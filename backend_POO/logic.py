import model
import connect
# Librería webbrowser esta incluida por defecto, será usada para abrir una dirección en el navegador
import webbrowser
# from datetime import datetime, date, time, timezone
# Librería datetime esta incluida por defecto, permite la correcta elaboración para formatos de fecha
# import datetime
from datetime import datetime, timedelta
# Librería smtplib esta incluida por defecto, permite la creación y envío de correos electrónicos
import smtplib
# Librería incluida por defecto, MIMEMultipart con el fin de organizar los datos relacionados a la aplicación de correos electrónicos (remitente y destinatario)
from email.mime.multipart import MIMEMultipart
# Librería incluida por defecto, se importa MIMEText para permitir la redacción del mensaje a enviar por correo electrónico
from email.mime.text import MIMEText


class Persona:
    def __init__(self) -> None:
        self.persona = model.Persona()
        self.metodosConexionPersona = connect.Persona()

    def crearUsuario(self, info):
        if info != None:
            self.persona = info
            self.metodosConexionPersona.setPersona(self.persona)

    def consultarUsuario(self,id):
        resultado = self.metodosConexionPersona.getPersona(id)
        return resultado
    
    def desafiliarUsuario(self, persona):
        if persona != None:
            self.persona = persona
            self.metodosConexionPersona.updatePersona(self.persona)

    def consultarEstadoPersonaCitada(self, id):
        resultado = self.metodosConexionPersona.getEstadoPersonaCitada(id)
        return resultado

    # Función para cambiar estado de vacunación de un usuario si cumple con los requisitos
    def vacunarPacientes(self, persona):
        if persona != None:
            self.persona = persona
            self.metodosConexionPersona.setPacienteVacunado(self.persona)

    def documentacionDeUsuario(self):
        pass

class Lote:
    def __init__(self) -> None:
        self.lote = model.Lote()
        self.metodosConexionLote = connect.Lote()

    def crearLote(self, info):
        if info != None:
            self.lote = info
            self.metodosConexionLote.setLote(self.lote)

    def consultarLote(self,id):
        resultado = self.metodosConexionLote.getLote(id)
        return resultado
    
    def consultarLotes(self):
        resultados = self.metodosConexionLote.getLotes()
        return resultados
    
    def reiniciarValores(self):
        self.metodosConexionLote.setValoresVacunasDefault()

class PlanDeVacunacion:
    def __init__(self) -> None:
        self.plan = model.PlanDeVacunacion()
        self.metodosConexionPlan = connect.PlanDeVacunacion()

    def crearPlanVacunacion(self, info):
        if info != None:
            self.plan = info
            self.metodosConexionPlan.setPlan(self.plan)

    def consultarPlanVacunacion(self,id):
        resultado = self.metodosConexionPlan.getPlan(id)
        return resultado

    def consultarPlanesVacunacion(self):
        resultado = self.metodosConexionPlan.getPlanes()
        return resultado
    
    def consultarRangoEdades(self):
        rangoEdades = self.metodosConexionPlan.getRangoEdades()
        return rangoEdades
    
    def verificarEdad(self, edad):
        rangoEdades = self.consultarRangoEdades()
        flag = True
        for rango in rangoEdades:
            if rango[0] <= edad <= rango[1]:
                flag = False
                message = 'La edad seleccionada se encuentra dentro de otro rango'
                return (flag, message)
        return (flag,)

class ProgramacionDeVacunas(Persona, Lote, PlanDeVacunacion):
    def __init__(self) -> None:
        self.programacion = model.ProgramacionDeVacunas()
        self.metodosConexionProgramacion = connect.ProgramacionDeVacunas()
        self.metodosConexionPlan = connect.PlanDeVacunacion()

    def crearProgramacion(self, fechaInicioIngresada):
        self.metodosConexionProgramacion.reiniciarProgramacion()
        retornoInfoVacunas = self.programacionPacienteLote()
        retornoInfoProgramacion = self.programacionFechaHora(fechaInicioIngresada)
        if not retornoInfoVacunas[0]:
            return retornoInfoVacunas[1], retornoInfoProgramacion[1]
        return False, retornoInfoProgramacion[1]

    def programacionPacienteLote(self):
        planesVacunacion = self.metodosConexionPlan.getPlanes()
        message = ''
        flag = True
        for plan in planesVacunacion:
            pacientesAVacunar = self.metodosConexionProgramacion.getPacientesAVacunar(plan.edadMinima, plan.edadMaxima)
            if pacientesAVacunar:
                for persona in pacientesAVacunar:
                    lote = self.metodosConexionProgramacion.getVacunaDisponible()
                    if lote:
                        self.metodosConexionProgramacion.setProgramacion(persona, lote, plan)
                    else:
                        message = 'Limite de vacunas alcanzado'
                        flag = lote
        return(flag, message)

    def programacionFechaHora(self, fechaInicioIngresadaDt):
        citasAProgramar = self.metodosConexionProgramacion.getCitasAProgramar()
        for i in citasAProgramar:
            self.programacion = i[0]
            plan = i[1]
            persona = i[2]
            lote = i[3]
            ultimaCitaProgramada = self.metodosConexionProgramacion.getUltimacita()
            fechaInicioDt = datetime.strptime(plan.fechaInicio, "%Y-%m-%d")
            if fechaInicioIngresadaDt > fechaInicioDt:
                fechaInicioDt = fechaInicioIngresadaDt
            fechaFinDt = datetime.strptime(plan.fechaFinal, "%Y-%m-%d")
            if not ultimaCitaProgramada:
                fechaActual = datetime.now()
                if fechaInicioDt > fechaActual:
                    self.programacion.fechaProgramada = fechaInicioDt.strftime("%Y-%m-%d")
                else:
                    fechaCitaDt = fechaActual + timedelta(days=1)
                    self.programacion.fechaProgramada = fechaCitaDt.strftime("%Y-%m-%d")
                self.programacion.horaProgramada = self.programacion.horaInicio
            else:
                fechaMaxima = ultimaCitaProgramada.fechaProgramada
                horaMaxima = ultimaCitaProgramada.horaProgramada
                hora = int(horaMaxima[0:2])
                hora += 1
                # se da la fecha y hora almacenándola en dt con el método datetime.strptime()
                if hora >= int(self.programacion.horaFin[0:2]):
                    self.programacion.horaProgramada = self.programacion.horaInicio
                    dt = datetime.strptime(fechaMaxima, "%Y-%m-%d")
                    fechaCitaDt = dt + timedelta(days=1)
                    self.programacion.fechaProgramada = fechaCitaDt.strftime("%Y-%m-%d")
                # Se agrega la hora conseguida a (self.programacion.horaProgramada)
                else:
                    self.programacion.horaProgramada = '{}:00:00'.format(hora)
                    if hora < 10:
                        self.programacion.horaProgramada = '0{}:00:00'.format(hora)
                    # Se iguala la fecha de la cita obtenida (self.programacion.fechaProgramada) como la fecha maxima que se tiene (fechaMaxima)
                    self.programacion.fechaProgramada = fechaMaxima

                fechaCitaDt = datetime.strptime(self.programacion.fechaProgramada, "%Y-%m-%d")
                # en caso de que el valor de (self.programacion.fechaProgramadaDt) sea menor a (fechaInicioDt), se le asigna el valor de (horaInicio) a (self.programacion.horaProgramada)
                if fechaCitaDt < fechaInicioDt:
                    self.programacion.fechaProgramada = fechaInicioDt.strftime("%Y-%m-%d")
                    self.programacion.horaProgramada = self.programacion.horaInicio
            fechaCitaDt = datetime.strptime(self.programacion.fechaProgramada, "%Y-%m-%d")
            if fechaCitaDt > fechaFinDt:
                continue
            self.metodosConexionProgramacion.setFechaHora(self.programacion)
            # self.enviarCorreo(persona.correo, self.programacion.fechaProgramada, self.programacion.horaProgramada, lote.fabricante)
        return (True, 'Programación de citas de vacunacion exitosa')
    
    def enviarCorreo(destinatario, dia, hora, vacuna):
        # se crea el mensaje electrónico con todos sus componentes como (mensajeObj) con la función MIMEMultipart() del repositorio email.mime.multipart
        mensajeObj = MIMEMultipart()
        # se crea la variable que contendrá el mensaje (mensaje)
        mensaje = '''Cordial saludo.
        Le notificamos que su cita de vacunacion esta programada para el dia {} a las {}. Le sera aplicada la vacuna {}.'''

        # se crean variables de remitente, destinatario, asunto y contraseña se correo emisor
        mensajeObj['From'] = 'pruebas.vacunacion@gmail.com'
        mensajeObj['To'] = destinatario
        mensajeObj['Subject'] = 'Email de prueba'
        password = 'TEST_123*'
        # se adjuntan valores al mensaje con el método .attach()
        mensajeObj.attach(MIMEText(mensaje.format(dia, hora, vacuna), 'plain'))

        # Por medio del método smtplib.SMTP() se inicia una sesión para enviar el mensaje electrónico
        try:
            server = smtplib.SMTP('smtp.gmail.com: 587')
            # se activa el método almacenado en (server) con el método .starttls()
            server.starttls()
            # Se da inicio de sesión con el método server.login()
            server.login(mensajeObj['From'], password)
            # Se adjunta y envía el correo con el método server.sendmail()
            server.sendmail(mensajeObj['From'], mensajeObj['To'], mensajeObj.as_string())
            message = 'correo enviado'
            # Se realiza el cierre de la conexión con el método .quit()
            server.quit()
        # se imprimirá "error" si ha ocurrido una excepción
        except:
            message = 'error'
        finally:
            return message  

    def consultarProgramacionCompleta(self, datoConsulta):
        datosConsulta = ('pc.noId', 'pc.nombre', 'pc.apellido', 'pc.direccion', 'pc.telefono', 'pc.correo', 'pgv.fechaProgramada', 'pgv.horaProgramada', 'lv.noLote', 'lv.fabricante')
        resultados = self.metodosConexionProgramacion.getProgramacionCompleta(datosConsulta[datoConsulta])
        return resultados

    # Función para programar la vacunación de un usuario individual
    def consultarProgramacionIndividual(self, id):
        resultado = self.metodosConexionProgramacion.getProgramacionIndividual(id)
        return resultado


def crearTablas():
    connect.crearTablas()

# Función para abrir documentación de usuario
def documentacionUsuario():
    # Se almacena un link correspondiente a la ubicación del pdf
    path = 'https://drive.google.com/file/d/1L8BBeJP-mc_QLmNplzYemZgxe4j1F_Bx/view?usp=sharing'
    # Abrimos el archivo en el navegador siguiendo la variable (path) por el método webbrowser.open_new() de la librería webbrowser
    webbrowser.open_new(path)
