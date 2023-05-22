
def repetirespañol ():
    respuesta=0
    while respuesta != "si" and respuesta != "no":
        respuesta = input ("Quieres probar otro tema? ")
    print ("")
    return respuesta

def repetiringles ():
    respuesta=0
    while respuesta != "si" and respuesta != "no":
        respuesta = input ("You want to chose another topic? ")
    print ("")
    return respuesta

def desktop_ing ():
    def PreguntaRepetida (arg):
        respuesta=0
        while respuesta != "yes" and respuesta != "no":
            respuesta = input (arg)
        print ("")
        return respuesta

    pregunta01=("WHY IS MY DESKTOP COMPUTER NOT TURNING ON?  ")
    respuesta=PreguntaRepetida (pregunta01)
    if respuesta == "yes":
        print (" Check all cables are securely connected")
        print ("Unplug everything except screen, mouse, and keyboard")
        print ("Open the PC and check power supply connectors")
    else:
        pregunta02=("WHY IS MY COMPUTER MAKING STRANGE BEEPS WHEN I SWITCH IT ON? ")
        respuesta=PreguntaRepetida (pregunta02)
        if respuesta == "yes":
            print ("Make a note of the beep pattern (e.g. three short beeps)")
            print ("Google your computer manufacturer and model name, then 'beep codes'")
        else:
            pregunta03= ("HOW CAN I TELL IF MY COMPUTER IS OVERHEATING? ")
            respuesta=PreguntaRepetida (pregunta03)
            if respuesta == "yes":
                print ("Download Speccy")
                print ("Check CPU and graphics card temperatures")
                print ("Switch off if too hot")
            else:
                pregunta04=("WHY IS THERE NO SOUND COMING FROM MY COMPUTER'S EXTERNAL SPEAKERS? ")
                respuesta=PreguntaRepetida (pregunta04)
                if respuesta == "yes":
                    print ("Check power to the speakers")
                    print ("Ensure the right speakers are selected in Windows/macOS")
                    print ("Check the Bluetooth connection for wireless speakers")
                else:
                    pregunta05=("WHY ARE GAMES RUNNING REALLY SLOWLY ON MY COMPUTER? ")
                    respuesta=PreguntaRepetida (pregunta05)
                    if respuesta == "yes":
                        print ("Invest in a new graphics card (if possible)")
                        print ("Dial down the game's graphics quality or resolution")
                        print ("Consider a games-streaming service")
                    else:
                        pregunta06=("WHY WON'T THE USB PORT ON MY COMPUTER CHARGE MY PHONE? ")
                        respuesta=PreguntaRepetida (pregunta06)
                        if respuesta == "yes":
                            print ("Don't let the computer lapse into sleep/standby mode")
                            print ("Check you're using the correct USB port")
                            print ("Make sure Always-on USB is enabled")
                        else:
                            pregunta07=("MY PC IS ASKING ME TO UPDATE THE BIOS - SHOULD I DO IT? ")
                            respuesta=PreguntaRepetida (pregunta07)
                            if respuesta == "yes":
                                print ("Make sure it's not a fake pop-up")
                                print ("Save all work and close all programs")
                                print ("Plug a laptop in and then run the update")
                            else:
                                pregunta08=("WHY DOESN' T MY COMPUTER RECOGNISE MY MEMORY CARD? ")
                                respuesta=PreguntaRepetida (pregunta08)
                                if respuesta == "yes":
                                    print ("Keep the card in the camera and transfer images using a cable or Wi-Fi")
                                    print ("Use recovery software such as Recuva to rescue corrupted cards")
                                else:
                                    pregunta09=("WHAT IS THE BLUE SCREEN OF DEATH? ")
                                    respuesta=PreguntaRepetida (pregunta09)
                                    if respuesta == "yes":
                                        print  ("Make a quick note of any error message")
                                        print  ("Google that error code to find out what caused the crash")
                                        print  ("Update graphics drivers if Blue Screens of Death are persistent")
                                    else:
                                        pregunta10=("WHY IS MY COMPUTER SO SLOW? ")
                                        respuesta=PreguntaRepetida (pregunta10)
                                        if respuesta == "yes":
                                            print ("Too many programs loading at startup")
                                            print ("Running out of storage space")
                                            print ("Your system is riddled with malware")
                                            print ("Too many or rogue browser tabs")
                                            print ("You're in the wrong power mode")
                                            print ("You've just installed a major Windows update")
                                            print ("Your computer is getting on a bit")
                                        else:
                                            pregunta11=("WHY HAVE ALL THE ICONS ON MY WINDOWS DESKTOP GONE MISSING? ")
                                            respuesta=PreguntaRepetida (pregunta11)
                                            if respuesta == "yes":
                                                print  ("Right-click on desktop, select View, and then Show Desktop Icons")
                                                print  ("Look for missing icons in Recycle Bin")
                                                print  ("Create a new shortcut by dragging from Start menu")
                                            else:
                                                pregunta12=("WHEN I SWITCH ON MY COMPUTER, I SEE A DEMAND FOR MONEY TO GIVE ME MY FILES BACK. WHAT SHOULD I DO? ")
                                                respuesta=PreguntaRepetida (pregunta12)
                                                if respuesta == "yes":
                                                    print  ("Check whether you can still open files")
                                                    print  ("Restore your PC from a backup")
                                                    print  ("See if you can download a decryptor or revive deleted files")
                                                else:
                                                    pregunta13=("HOW DO I GET RID OF THE AWFUL CORTANA? ")
                                                    respuesta=PreguntaRepetida (pregunta13)
                                                    if respuesta == "yes":
                                                        print  ("Disable Cortana from the Cortana Permissions setting")
                                                        print  ("Remove the Cortana button from the Windows taskbar")
                                                        print  ("Install the free Alexa app if you want a worthwhile replacement")
                                                    else:
                                                        pregunta14=("WAYS YOU CAN BREAK YOUR COMPUTER ALL BY YOURSELF ")
                                                        respuesta=PreguntaRepetida (pregunta14)
                                                        if respuesta == "yes":
                                                            print ("1. Not uninstalling programs properly")
                                                            print ("2. Turning on very cold laptops")
                                                            print ("3. Downloading 'freebies' from dodgy sites")
                                                            print ("4. Answering a phone call from Microsoft")
                                                            print ("5. Installing fix-it utilities")
                                                            print ("6. Run without security software")
                                                            print ("7. Powering down during Windows updates")
                                                            print ("8. Tinkering with the Registry")
                                                            print ("9. Getting in over your head")
                                                            print ("10. Giving the kids admin rights")
                                                        else:
                                                            pregunta15=("WHY IS MY COMPUTER MAKING A SCRATCHING NOISE? ")
                                                            respuesta=PreguntaRepetida (pregunta15)
                                                            if respuesta == "yes":
                                                                print ("Switch off the computer immediately")
                                                                print ("Rely on your data backups and replace the disk, or...")
                                                                print ("...send the broken disk to a data recovery specialist")
                                                            else:
                                                                pregunta16=("MY USB HARD DISK IS NOT RECOGNISED WHEN I PLUG IT INTO MY COMPUTER? ")
                                                                respuesta=PreguntaRepetida (pregunta16)
                                                                if respuesta == "yes":
                                                                    print ("Reinstall the disk drive")
                                                                    print ("Reinstall the USB controller drivers")
                                                                    print ("Assign the drive a letter in Windows")
                                                                else:
                                                                    respuesta=repetiringles ()
                                                                    if respuesta == "si":
                                                                        respuesta=0
                                                                        while respuesta != "laptop" and respuesta != "peripherals" and respuesta != "windows" and respuesta != "screen":
                                                                            print (" Options:")
                                                                            print ("  - laptop")
                                                                            print ("  - peripherals")
                                                                            print ("  - windows")
                                                                            print ("  - screen")
                                                                            respuesta = input ("Select one: ")
                                                                        print ("")

def sobremesa_es () :
    def PreguntaRepetida (arg):
        respuesta=0
        while respuesta != "si" and respuesta != "no":
            respuesta = input (arg)
        print ("")
        return respuesta

    pregunta01=("POR QUE NO SE ENCIENDE MI ORDENADOR DE SOBREMESA? ")
    respuesta=PreguntaRepetida (pregunta01)
    if respuesta == "si":
        print ("Compruebe que todos los cables estan bien conectados")
        print ("Desenchufe todo excepto la pantalla, el raton y el teclado")
        print ("Abra el PC y compruebe los conectores de la fuente de alimentacion")
    else:
        pregunta02=("WHY IS MY COMPUTER MAKING STRANGE BEEPS WHEN I SWITCH IT ON? ")
        respuesta=PreguntaRepetida (pregunta02)
        if respuesta == "si":
            print ("Anote el patron de pitidos (por ejemplo, tres pitidos cortos)")
            print ("Busca en Google el fabricante y el nombre del modelo de tu ordenador, y luego 'codigos de pitidos'.")
        else:
            pregunta03= ("COMO PUEDO SABER SI MI ORDENADOR SE ESTA SOBRECALENTANDO? ")
            respuesta=PreguntaRepetida (pregunta03)
            if respuesta == "si":
                print ("Descargar Speccy")
                print ("Compruebe la temperatura de la CPU y de la tarjeta grafica")
                print ("Apague si esta demasiado caliente")
            else:
                pregunta04=("POR QUE NO SALE SONIDO DE LOS ALTAVOCES EXTERNOS DE MI ORDENADOR? ")
                respuesta=PreguntaRepetida (pregunta04)
                if respuesta == "si":
                    print ("Comprobar la alimentacion de los altavoces")
                    print ("Asegurese de que los altavoces correctos estan seleccionados en Windows/macOS")
                    print ("Comprueba la conexion Bluetooth de los altavoces inalambricos")
                else:
                    pregunta05=("POR QUE LOS JUEGOS VAN MUY LENTOS EN MI ORDENADOR? ")
                    respuesta=PreguntaRepetida (pregunta05)
                    if respuesta == "si":
                        print ("Invertir en una nueva tarjeta grafica (si es posible)")
                        print ("Bajar la calidad de los graficos o la resolucion del juego")
                        print ("Considere un servicio de transmision de juegos")
                    else:
                        pregunta06=("POR QUE EL PUERTO USB DE MI ORDENADOR NO CARGA MI TELEFONO? ")
                        respuesta=PreguntaRepetida (pregunta06)
                        if respuesta == "si":
                            print ("No dejes que el ordenador entre en modo de suspension/espera")
                            print ("Compruebe que esta utilizando el puerto USB correcto")
                            print ("Asegurese de que el USB siempre activo esta activado")
                        else:
                            pregunta07=("MI PC ME PIDE QUE ACTUALICE LA BIOS - DEBO HACERLO? ")
                            respuesta=PreguntaRepetida (pregunta07)
                            if respuesta == "si":
                                print ("Asegurese de que no es una ventana emergente falsa")
                                print ("Guardar todo el trabajo y cerrar todos los programas")
                                print ("Conecte un ordenador portatil y ejecute la actualizacion")
                            else:
                                pregunta08=("POR QUE MI ORDENADOR NO RECONOCE MI TARJETA DE MEMORIA? ")
                                respuesta=PreguntaRepetida (pregunta08)
                                if respuesta == "si":
                                    print ("Mantenga la tarjeta en la camara y transfiera las imagenes mediante un cable o Wi-Fi")
                                    print ("Utiliza un software de recuperacion como Recuva para rescatar las tarjetas danyadas")
                                else:
                                    pregunta09=("QUE ES LA PANTALLA AZUL DE LA MUERTE? ")
                                    respuesta=PreguntaRepetida (pregunta09)
                                    if respuesta == "si":
                                        print  ("Anote rapidamente cualquier mensaje de error")
                                        print  ("Busque en Google ese codigo de error para averiguar la causa del fallo")
                                        print  ("Actualizar los controladores graficos si las Pantallas Azules de la Muerte son persistentes")
                                    else:
                                        pregunta10=("POR QUE MI ORDENADOR VA TAN LENTO? ")
                                        respuesta=PreguntaRepetida (pregunta10)
                                        if respuesta == "si":
                                            print ("Demasiados programas cargando al inicio")
                                            print ("Se esta agotando el espacio de almacenamiento")
                                            print ("Su sistema esta plagado de malware")
                                            print ("Demasiadas pestanyas o pestanyas de navegador no deseadas")
                                            print ("Estas en el modo de energia equivocado")
                                            print ("Acaba de instalar una actualizacion importante de Windows")
                                            print ("Su ordenador se esta poniendo un poco")
                                        else:
                                            pregunta11=("POR QUE HAN DESAPARECIDO TODOS LOS ICONOS DE MI ESCRITORIO DE WINDOWS? ")
                                            respuesta=PreguntaRepetida (pregunta11)
                                            if respuesta == "si":
                                                print  ("Haga clic con el boton derecho del raton en el escritorio,seleccione Ver y, a continuacion, Mostrar iconos del escritorio")
                                                print  ("Busque los iconos que faltan en la papelera de reciclaje")
                                                print  ("Crear un nuevo acceso directo arrastrando desde el menu Inicio")
                                            else:
                                                pregunta12=("CUANDO ENCIENDO MI ORDENADOR, VEO UNA PETICION DE DINERO PARA DEVOLVERME MIS ARCHIVOS. QUE DEBO HACER? ")
                                                respuesta=PreguntaRepetida (pregunta12)
                                                if respuesta == "si":
                                                    print  ("Comprueba si todavia puedes abrir archivos ")
                                                    print  ("Restaura tu PC desde una copia de seguridad")
                                                    print  ("Comprueba si puedes descargar un desencriptador o revivir los archivos eliminados")
                                                else:
                                                    pregunta13=("COMO ME DESHAGO DE LA HORRIBLE CORTANA? ")
                                                    respuesta=PreguntaRepetida (pregunta13)
                                                    if respuesta == "si":
                                                        print  ("Desactivar Cortana desde la configuracion de permisos de Cortana ")
                                                        print  ("Eliminar el boton de Cortana de la barra de tareas de Windows")
                                                        print  ("Instala la aplicacion gratuita Alexa si quieres un reemplazo que valga la pena")
                                                    else:
                                                        pregunta14=("QUIERES VER FORMAS DE ROMPER TU ORDENADOR TU SOLO? ")
                                                        respuesta=PreguntaRepetida (pregunta14)
                                                        if respuesta == "si":
                                                            print ("1. No se desinstalan correctamente los programas")
                                                            print ("2. Encendido de ordenadores portatiles muy frios")
                                                            print ("3. Descarga de 'regalos' de sitios dudosos")
                                                            print ("4. Responder a una llamada telefonica de Microsoft")
                                                            print ("5. Instalacion de utilidades de reparacion")
                                                            print ("6. Ejecutar sin software de seguridad")
                                                            print ("7. Apagado durante las actualizaciones de Windows")
                                                            print ("8. Jugueteando con el Registro")
                                                            print ("9. Enfrascarse en lo que no se puede hacer")
                                                            print ("10. Dar a los ninyos derechos de administrador")
                                                        else:
                                                            pregunta15=("POR QUE MI ORDENADOR HACE UN RUIDO DE ARANYAZOS? ")
                                                            respuesta=PreguntaRepetida (pregunta15)
                                                            if respuesta == "si":
                                                                print ("Apagar el ordenador inmediatamente")
                                                                print ("Confie en sus copias de seguridad de datos y sustituya el disco, o...")
                                                                print ("...enviar el disco roto a un especialista en recuperacion de datos")
                                                            else:
                                                                pregunta16=("MI DISCO DURO USB NO ES RECONOCIDO CUANDO LO CONECTO A MI ORDENADOR? ")
                                                                respuesta=PreguntaRepetida (pregunta16)
                                                                if respuesta == "si":
                                                                    print ("Reinstalar la unidad de disco")
                                                                    print ("Vuelva a instalar los controladores del controlador USB ")
                                                                    print ("Asigne una letra a la unidad en Windows")
                                                                else:
                                                                    respuesta=repetirespañol ()
                                                                    if respuesta == "si":
                                                                        respuesta=0
                                                                        while respuesta != "portatil" and respuesta != "perifericos" and respuesta != "windows" and respuesta != "pantalla":
                                                                            print (" Opciones:")
                                                                            print ("  - portatil")
                                                                            print ("  - perifericos")
                                                                            print ("  - windows")
                                                                            print ("  - pantalla")
                                                                            respuesta = input ("Elige una: ")
                                                                        print ("")
                                                                        espanyol1 (respuesta)
                                                                        return respuesta

def screen_ing () :
    def PreguntaRepetida (arg):
        respuesta=0
        while respuesta != "yes" and respuesta != "no":
            respuesta = input (arg)
        print ("")
        return respuesta

    pregunta1=("WHAT ARE THOSE BLACK DOTS ON MY SCREEN? ")
    respuesta = PreguntaRepetida (pregunta1)
    if respuesta == "yes":
        print ("Visit color.aurlien.net to check for dead or stuck pixels")
        print ("Go to jscreenfix.com to unjam stuck pixels")
    else:
        pregunta2=("MY COMPUTER SCREEN IS DIRTY HOW DO I CLEAN IT")
        respuesta=PreguntaRepetida (pregunta2)
        
        if respuesta == "yes":
            print ("Use a microfibre cloth")
            print ("Dont spray water/cleaners directly onto the screen") 
            print ("Dont press too hard")
        else:
            pregunta3=("MY COMPUTER'S TOUCHSCREEN HAS STOPPED WORKING!")
            respuesta=PreguntaRepetida (pregunta3)

            if respuesta == "yes":
                print ("Check for new display/graphics drivers")
                print ("Disable touchscreen power managemente") 
                print ("Run BIOS diagnostics tests")
            else:
                pregunta4= ("WHY HAS MY LAPTOP SCREEN GONE VERY DIM?")
                respuesta=PreguntaRepetida (pregunta4)
                
                if respuesta == "yes":
                    print ("Adjust the power management settings")
                    print ("Turn off adaptive brightness") 
                    print ("Make sure you're not in night mode ")
                else:
                    pregunta5= ("WHY WON'T THE EXTERNAL SCREEN PLUGGED INTO MY LAPTOP WORK?")
                    respuesta=PreguntaRepetida(pregunta5)

                    if respuesta == "yes":
                        print ("Adjust the power management settings")
                        print ("Turn off adaptive brightness") 
                        print ("Make sure you're not in night mode ")
                    else:
                        pregunta6= ("MY PC'S FANS ARE CLOGGED WITH DUST HOW DO I CLEAN THEM?")
                        respuesta=PreguntaRepetida(pregunta6)

                        if respuesta == "yes":
                            print ("Take anti-static protection")
                            print ("Arm yourself with a can of compressed air, cotton buds, and a cloth")
                            print ("Clean any fans and vents to prevent overheating")
                        else:
                            respuesta=repetiringles ()
                            if respuesta == "si":
                                respuesta=0
                                while respuesta != "laptop" and respuesta != "peripherals" and respuesta != "desktop" and respuesta != "windows" :
                                    print (" Options:")
                                    print ("  - laptop")
                                    print ("  - peripherals")
                                    print ("  - desktop")
                                    print ("  - windows")
                                    respuesta = input ("Select one: ")
                                print ("")
                                ingles1 (respuesta)

def peripherals_ing () :
    def PreguntaRepetida (arg):
            respuesta=0
            while respuesta != "yes" and respuesta != "no":
                respuesta = input (arg)
            print ("")
            return respuesta

    pregunta1=("WHY IS MY MOUSE NOT WORKING?")
    respuesta = PreguntaRepetida (pregunta1)
    if respuesta == "yes":
        print ("Try different USB ports")
        print ("Use Windows' Mouse Keys to help you diagnose faults")
        print ("Make sure the batteries are charged")
    else:
        pregunta2=("WHY CANT MY COMPUTER SEE MY PRINTER?")
        respuesta=PreguntaRepetida (pregunta2)
            
        if respuesta == "yes":
            print ("Check the printer and computer are on the same wireless band")
            print ("Set the printer as the default printer in Windows/Mac")
            print ("Run the printer troubleshooter")
        else:
            respuesta=repetiringles ()
            if respuesta == "si":
                respuesta=0
                while respuesta != "laptop" and respuesta != "desktop" and respuesta != "windows" and respuesta != "screen":
                    print (" Options:")
                    print ("  - laptop")
                    print ("  - desktop")
                    print ("  - windows")
                    print ("  - screen")
                    respuesta = input ("Select one: ")
                print ("")
                ingles1 (respuesta)

def windows_ing () :
    def PreguntaRepetida (arg):
            respuesta=0
            while respuesta != "yes" and respuesta != "no":
                respuesta = input (arg)
            print ("")
            return respuesta

    pregunta1=("MY COMPUTER HAS BROKEN AFTER A WINDOWS UPDATE WHAT NOW?")
    respuesta=PreguntaRepetida(pregunta1)
    if  respuesta == "yes":
            print ("Roll back or uninstall the updates")
            print ("Use System Restore to return to a working configuration")
            print ("Block broken updates from re-installing")
            print ("Use the troubleshooting settings to repair a system that won't start")
    else:
        pregunta2=("I'VE FORGOTTEN MY WINDOWS 10 PASSWORD HOW DO I GET INTO MY COMPUTER?")
        respuesta=PreguntaRepetida (pregunta2)

        if respuesta == "yes":
            print ("Use the Microsoft Account recovery website")
            print ("Try an alternative login method (if previously set up")
            print ("Use another admin account on the same PC")
        else:
            pregunta3=("MY COMPUTER IS HORRIBLY SLOW. HOW DO I REINSTALL WINDOWS 10?")
            respuesta=PreguntaRepetida (pregunta3)
            if respuesta == "yes":
                print ("Backup the PC (if possible")
                print ("Reset the PC from within Windows or the recovery tools")
                print ("Reinstall Windows from a USB stick if the above won't work")

            else:
                pregunta4=("WHY HAVE ALL THE ICONS ON MY WINDOWS DESKTOP GONE MISSING?")
                respuesta=PreguntaRepetida (pregunta4)

                if respuesta == "yes":
                    print ("Right-click on desktop, select View, and then Show Desktop Icons")
                    print ("Look for missing icons in Recycle Bin")
                    print (" Create a new shortcut by dragging from Start menu")

                else:
                    pregunta5=("WINDOWS WON'T OPEN A FILE BECAUSE IT ‘HASN'T GOT AN APP ASSOCIATED WITH IT'. WHAT DO I DO?")
                    respuesta=PreguntaRepetida (pregunta5)
                    
                    if respuesta == "yes":
                        print ("Select file properties to identify the file type")
                        print ("Right-click on file and choose Open With to find the relevant app")
                        print ("Or use the Windows Default App settings")

                    else:
                        pregunta6=("WHY HAS THE WINDOWS 10 SEARCH BOX GONE MISSING?")
                        respuesta=PreguntaRepetida (pregunta6)

                        if respuesta == "yes":
                            print ("Access the search options by right-clicking on the taskbar")
                            print ("Choose whether you want the full bar back or just a search icon")
                        else:
                            pregunta7=("HOW DO I GET RID OF THE AWFUL CORTANA?")
                            respuesta=PreguntaRepetida (pregunta7)

                            if respuesta == "yes":
                                print ("Disable Cortana from the Cortana Permissions setting")
                                print ("Remove the Cortana button from the Windows taskbar")
                                print ("Install the free Alexa app if you want a worthwhile replacement")

                            else:
                                pregunta8=("I DON'T THINK MY PC HAS UPDATED TO THE LATEST VERSION OF WINDOWS – HOW DO I FORCE IT TO DO SO?")
                                respuesta=PreguntaRepetida (pregunta8)

                                if respuesta == "yes":
                                    print ("Check the About Your PC screen to find out what version you're on")
                                    print ("Check Microsoft's site to find out what the latest release is")
                                    print ("Use the Check for Updates screen to download any new updates")

                                else:
                                    pregunta9=("MY WINDOWS 7 PC KEEPS FLASHING UP WARNINGS THAT SUPPORT HAS ENDED. WHAT DOES THAT MEAN?")
                                    respuesta=PreguntaRepetida (pregunta9)

                                    if respuesta == "yes":
                                        print ("Seek out Windows 7 security software")
                                        print ("Upgrade to Windows 10")
                                        print ("Replace Windows 7 with CloudReady or a Linux operating system ")
                                    else:
                                        respuesta=repetiringles ()
                                        if respuesta == "si":
                                            respuesta=0
                                            while respuesta != "laptop" and respuesta != "peripherals" and respuesta != "desktop" and respuesta != "screen":
                                                print (" Options:")
                                                print ("  - laptop")
                                                print ("  - peripherals")
                                                print ("  - desktop")
                                                print ("  - screen")
                                                respuesta = input ("Select one: ")
                                            print ("")
                                            ingles1 (respuesta)

def laptop_ing ():
    def preguntarepe (arg):
        respuesta=("0")
        while (respuesta != "yes" and respuesta != "no"):
            respuesta = input (arg)
        return respuesta

    respuesta1=("Why is my lapton not turning on?")
    respuesta = preguntarepe (respuesta1)
    if respuesta == "yes" :
        print ("Check power cables are plugged in securely")
        print ("Only use the supplied charger")
        print ("Leave the battery to charge for a few hours")
        print ("Drain residual electricity from the computer")
    else:
        respuesta2=("Why is my laptop's keyboard not working?")
        respuesta = preguntarepe (respuesta2)
        if respuesta == "yes" :
            print ("Switch the laptop off and dry any spills")
            print ("Reinstall the keyboard's software driver")
        else:
            respuesta3=("Why is my laptop's touchpad not working?")
            respuesta = preguntarepe (respuesta3)
            if respuesta == "yes" :
                print ("Check the mouse settings to make sure the touchpad hasn't been accidentally deactivated")
                print ("Update the touchpad's drivers")
                print ("Remove external mice")
            else:
                respuesta4=("Why is there no sound coming from my laptop's built-in speakers")
                respuesta = preguntarepe (respuesta4)
                if respuesta == "yes" :
                    print ("Switch off any Bluetooth headphones or speakers nearby")
                    print ("Check the computer's volume settings")
                    print ("Check browser tabs or applications aren't muted")
                    print ("Run the Windows troubleshooter")
                else:
                    respuesta5=("Can i make my laptop faster by upgrading its memory?")
                    respuesta = preguntarepe (respuesta5)
                    if respuesta == "yes" :
                        print ("Try Crucial's system scanner to see if you can upgrade your memory")
                        print ("Make sure you buy the right type")
                        print ("Double the quantity you already have to see a noticeable boost")
                    else:
                        respuesta6=("Why won't my laptop connect to the Wi-Fi?")
                        respuesta = preguntarepe (respuesta6)
                        if respuesta == "yes" :
                            print ("Check you've not accidentally disabled Wi-Fi")
                            print ("Restart both router and laptop")
                            print ("Wind back any recent wireless card driver updates")
                        else:
                            respuesta7=("How do i improve the battery life of my laptop?")
                            respuesta = preguntarepe (respuesta7)
                            if respuesta == "yes" :
                                print ("Dim the screen")
                                print ("Switch off Wi-Fi and Blueetoth")
                                print ("Dont leave the laptop chained to the mains")
                                print ("Switch off graphics chips")
                                print ("Disconnect peripherals")
                                print ("Dont put the laptop directly on your lap")
                                print ("Dont push it!!!!")
                            else:
                                respuesta8=("Can i replace my laptop's battery?")
                                respuesta = preguntarepe (respuesta8)
                                if respuesta == "yes" :
                                    print ("Run a battery report in Windows")
                                    print ("Check to see if your battery is reaplaceable")
                                    print ("Take a sealed unit for professional replacement")
                                else:
                                    respuesta9=("I've run out of USB ports - what now?")
                                    respuesta = preguntarepe (respuesta9)
                                    if respuesta == "yes" :
                                        print ("Get a USB hub")
                                        print ("Make sure to buy the right kind (Type-A, Type-C...) ")
                                        print ("Beware that some require external power")
                                    else:
                                        respuesta10=("My PC's fans are clogged with dust - how do i clean them?")
                                        respuesta = preguntarepe (respuesta10)
                                        if respuesta == "yes" :
                                            print ("Take anti-static protection")
                                            print ("Arm yourself with a can of compressed air, cotton buds, and a cloth")
                                            print ("Clean any fans and vents to prevent overheating")
                                        else:
                                            respuesta11=("Why whon't the external screen plugged into my laptop work?")
                                            respuesta = preguntarepe (respuesta11)
                                            if respuesta == "yes" :
                                                print ("Check the Windows/Mac display settings")
                                                print ("Make sure cables are plugged into correct port if using USB-C")
                                                print ("Update the display drivers")
                                            else:
                                                respuesta12=("My computer is horrible slow. How do i reinstall Windows 10?")
                                                respuesta = preguntarepe (respuesta12)
                                                if respuesta == "yes" :
                                                    print ("Backup the PC (if possible)")
                                                    print ("Reset the PC from within Windows or the recovery tools")
                                                    print ("Reinstall Windows from a USB stick if the above won't work")
                                                else: 
                                                    respuesta13=("Why have all the icons on my windows dekstop gone missing?")
                                                    respuesta = preguntarepe (respuesta13)
                                                    if respuesta == "yes" : 
                                                        print ("Right-click on the desktop, select View, and then Show Desktop icons")
                                                        print ("Look for missing icons in Recycle Bin")
                                                        print ("Create a new shortcut by dragging from Start Menu")
                                                    else:
                                                        respuesta14=("How do i make my laptop fans less noissy?")
                                                        respuesta = preguntarepe (respuesta14)
                                                        if respuesta == "yes" : 
                                                            print ("Drop back from maximum perfomance in the power plan")
                                                            print ("Buy a cheap laptop stand")
                                                            print ("Dont manually tinker with fans speeds!")
                                                        else:
                                                            respuesta=repetiringles ()
                                                            if respuesta == "si":
                                                                respuesta=0
                                                                while respuesta != "peripherals" and respuesta != "desktop" and respuesta != "windows" and respuesta != "screen":
                                                                    print (" Options:")
                                                                    print ("  - peripherals")
                                                                    print ("  - desktop")
                                                                    print ("  - windows")
                                                                    print ("  - screen")
                                                                    respuesta = input ("Select one: ")
                                                                print ("")
                                                                ingles1 (respuesta)

def portatil_es () :
    def preguntarepe (arg) :
        respuesta=("0")
        while (respuesta != "si" and respuesta != "no"):
            respuesta = input (arg)
        return respuesta

    respuesta1=("Tienes un problema para encender el Portatil?: ")
    respuesta = preguntarepe (respuesta1)   
    if respuesta == "si" :
        print ("Comprueba que los cables de alimentacion esten bien enchufados")
        print ("Utiliza el cargador original")
        print ("Comprueba que los cables de alimentacion esten bien enchufados")
        print ("Utiliza el cargador original")
        print ("Deja que la bateria se cargue durante 2 horas")
        print ("Drena la electricidad residual del ordenador")
    else:
        respuesta2=("Tienes un problema con el teclado del portatil?: ")
        respuesta = preguntarepe (respuesta2)
        if respuesta == "si" :
            print ("Primeramente comprueba que el portatil tiene bateria")
            print ("Comprueba que tu cable tiene la suficiente potencia")
            print ("Intenta cambiar de puerto, si tu portatil tiene USB C")
            print ("Si el portatil no ha sido enchufado durante unos meses, es posible que necesite un tiempo de enchufado")
            print ("Los ChromeBooks, a menudo necesitan estar enchufado durante varias horas antes de reanudar el funcionamiento")
        else:
            respuesta3=("Tienes un problema con el toucpad del portatil?: ")
            respuesta = preguntarepe (respuesta3)
            if respuesta == "si" : 
                print ("Comprueba que el touchpad no ha sido desactivado")
                print ("Actualiza los controaldores del touchpad")
                print ("Expulsa los posibles ratones conectados")
            else:
                respuesta4=("Tienes problemas con los altavoces de tu portatil?: ")
                respuesta = preguntarepe (respuesta4)
                if respuesta == "si" :
                    print ("Comprueba que no haya ningun dispositivo Blueetoth conectado")
                    print ("comprueba el volumen de tu portatil") 
                    print ("Comprueba que las pestanyas del navegador no esten silenciadas")
                    print ("Ejecuta el solucionador de problemas de Windows")
                else:
                    respuesta5=("Quieres mejorar el rendimiento de tu portatil?: ")
                    respuesta=preguntarepe (respuesta5)
                    if respuesta == "si" :
                        print ("Prueba el escaner Crucial para ver si puede actualizar su memoria")
                        print ("Comprueba que la RAM funciona a su velocidad maxima")
                        print ("Duplica la cantidad que ya tiene para ver una mejora notable")
                    else:
                        respuesta6=("Tienes problemas para conectare al Wi-Fi?: ")
                        respuesta=preguntarepe (respuesta6)
                        if respuesta == "si" : 
                            print ("Compruebe que el wifi no est a desactivado")
                            print ("Reinicia el router y/o el ordenador")
                            print ("Elimina la  ultima actualizacion del controlador de la tarjeta de Red")
                        else:
                            respuesta7=("Quieres mejorar la bateria de tu portatil?: ")
                            respuesta=preguntarepe (respuesta7)
                            if respuesta == "si" :
                                print ("Baja el brillo de la pantalla")
                                print ("Desconecta el Wi-Fi y el Blueetoth")
                                print ("Desconecta los perifericos")
                                print ("Desconecta los controladores gr aficos")
                                print ("No coloques el portatil encima de tus piernas o de tu cama")
                                print ("No le pidas el 100%")
                            else:
                                respuesta8=("Quieres sustituir la bateria de mi portatil?: ")
                                respuesta=preguntarepe (respuesta8)
                                if respuesta == "si" :
                                    print ("Ejecuta un informe de la bateria en Windows")
                                    print ("Comprueba si la bateria es reemplazadable")
                                    print ("Lleva una bateria sellada y oficial para sustituirla profesionalmente")
                                else:
                                    respuesta9=("Te has quedado sin puertos USB?: ")
                                    respuesta=preguntarepe (respuesta9)
                                    if respuesta == "si" :
                                        print ("Consigue un adaptador (hub) USB")
                                        print ("Asegurate de comprar el correcto, Tipo A, Tipo C...")
                                        print ("Ten en cuenta que algunos requieren alimentacion extra..")
                                    else:
                                        respuesta10=("Tienes problemas con el polvo en los ventiladores?")
                                        respuesta=preguntarepe (respuesta10)
                                        if respuesta == "si" :
                                            print ("Primero, consigue una pulsera antiestatica")
                                            print ("Compra aire comprimido, bastoncillos de algodon y un panyo de fibra")
                                            print ("Limpia los ventiladores para evitar el sobrecalentamiento")
                                        else:
                                            respuesta11=("Tienes un problema para conectar una pantalla externa?")
                                            respuesta=preguntarepe (respuesta11)
                                            if respuesta == "si" :
                                                print ("Comprueba la configuracion de pantalla de Windows/Mac")
                                                print ("Asegurate que los cables esten conectados en el puerto correcto")
                                                print ("Actualiza los controladores de la pantalla")
                                            else:
                                                respuesta12=("Quieres reinstalar Windows 10?")
                                                respuesta=preguntarepe (respuesta12)
                                                if respuesta == "si" :
                                                    print ("Haz una copia de seguridad del PC")
                                                    print ("Reinicia el PC desde Windows")
                                                    print ("Reinstala Windows desde una memoria USB booteable")
                                                else:
                                                    respuesta13=("Te han desaparecido los iconos del escritorio?")
                                                    respuesta=preguntarepe (respuesta13)
                                                    if respuesta == "si" :
                                                        print ("Haz click derecho con el raton en el escritorio y selecciona la opcion ver, despues mostrar iconos del escritorio")
                                                        print ("Busca los iconos que faltan en la papelera de reciclaje")
                                                        print ("Crea un nuevo acceso directo arrasntrandolo desde el menu de Inicio")
                                                    else:
                                                        respuesta14=("Tienes problemas de ruido con los ventiladores?")
                                                        respuesta=preguntarepe (respuesta14)
                                                        if respuesta == "si" :
                                                            print ("Reduce el rendimiento maximo en el plan de energia")
                                                            print ("Compra un soporte de portatil barato")
                                                            print ("No juegues manualmente con las velocidades de los ventiladores")
                                                        else:
                                                            respuesta=repetirespañol ()
                                                            if respuesta == "si":
                                                                respuesta=0
                                                                while respuesta != "perifericos" and respuesta != "sobremesa" and respuesta != "windows" and respuesta != "pantalla":
                                                                    print (" Opciones:")
                                                                    print ("  - perifericos")
                                                                    print ("  - sobremesa")
                                                                    print ("  - windows")
                                                                    print ("  - pantalla")
                                                                    respuesta = input ("Elige una: ")
                                                                print ("")
                                                                espanyol1 (respuesta)
                                                                return respuesta

def pantalla_es () :
    def PreguntaRepetida (arg):
        respuesta=0
        while respuesta != "si" and respuesta != "no":
            respuesta = input (arg)
        print ("")
        return respuesta
    
    pregunta1=("QUÉ SON ESOS PUNTOS NEGROS EN MI PANTALLA?")
    respuesta = PreguntaRepetida (pregunta1)
    if respuesta == "si":
        print ("Visite color.aurlien.net para verificar si hay píxeles muertos o atascados")
        print ("Vaya a jscreenfix.com para desbloquear píxeles atascados")
    else:
        pregunta2=("LA PANTALLA DE MI COMPUTADORA ESTÁ SUCIA CÓMO LA LIMPIO?")
        respuesta=PreguntaRepetida (pregunta2)
        
        if respuesta == "si":
            print ("Usa un paño de microfibra")
            print ("No rocíe agua/limpiadores directamente sobre la pantalla") 
            print ("No presione demasiado fuerte")
        else:
            pregunta3=("LA PANTALLA TÁCTIL DE MI ORDENADOR HA DEJADO DE FUNCIONAR!")
            respuesta=PreguntaRepetida (pregunta3)

            if respuesta == "si":
                print ("Buscar nuevos controladores de pantalla/gráficos")
                print ("Deshabilitar la administración de energía de la pantalla táctil") 
                print ("Ejecutar pruebas de diagnóstico del BIOS")
            else:
                pregunta4= ("POR QUÉ LA PANTALLA DE MI PORTÁTIL SE HA VUELTO MUY OSCURA?")
                respuesta=PreguntaRepetida (pregunta4)
                
                if respuesta == "si":
                    print ("Ajustar la configuración de administración de energía")
                    print ("Desactivar el brillo adaptable") 
                    print ("Asegúrate de no estar en modo noche")
                else:
                    pregunta5= ("POR QUÉ NO FUNCIONA LA PANTALLA EXTERNA CONECTADA A MI PORTÁTIL?")
                    respuesta=PreguntaRepetida(pregunta5)

                    if respuesta == "si":
                        print ("Compruebe la configuración de pantalla de Windows/Mac")
                        print ("Asegúrese de que los cables estén enchufados en el puerto correcto si usa USB-C") 
                        print ("Actualizar los controladores de pantalla")
                    else:
                        pregunta6= ("LOS VENTILADORES DE MI PC ESTÁN OBSTRUIDOS CON POLVO CÓMO LOS LIMPIO?")
                        respuesta=PreguntaRepetida(pregunta6)
                        if respuesta == "si":
                            print ("Lleva protección antiestática")
                            print ("Use una lata de aire comprimido, bastoncillos de algodón y un paño.")
                            print ("Limpie los ventiladores y las rejillas de ventilación para evitar el sobrecalentamiento.")
                        else:
                            respuesta=repetirespañol ()
                            if respuesta == "si":
                                respuesta=0
                                while respuesta != "portatil" and respuesta != "perifericos" and respuesta != "sobremesa" and respuesta != "windows" :
                                    print (" Opciones:")
                                    print ("  - portatil")
                                    print ("  - perifericos")
                                    print ("  - sobremesa")
                                    print ("  - windows")
                                    respuesta = input ("Elige una: ")
                                print ("")
                                espanyol1 (respuesta)
                                return respuesta

def windows_es () :
    def PreguntaRepetida (arg):
        respuesta=0
        while respuesta != "si" and respuesta != "no":
            respuesta = input (arg)
        print ("")
        return respuesta
    
    pregunta1=("MI COMPUTADORA SE HA ROTO DESPUÉS DE UNA ACTUALIZACIÓN DE WINDOWS ¿Y AHORA QUÉ?")
    respuesta=PreguntaRepetida(pregunta1)

    if respuesta == "si":
        print ("Revertir o desinstalar las actualizaciones")
        print ("Use Restaurar sistema para volver a una configuración de trabajo")
        print ("Bloquee las actualizaciones rotas para que no se vuelvan a instalar")
        print ("Use la configuración de solución de problemas para reparar un sistema que no se inicia")
    else:
        pregunta2=("HE OLVIDADO MI CONTRASEÑA DE WINDOWS 10 ¿CÓMO INGRESO A MI COMPUTADORA?")
        respuesta=PreguntaRepetida (pregunta2)
        if respuesta == "si":
            print ("Use el sitio web de recuperación de la cuenta de Microsoft")
            print ("Pruebe un método de inicio de sesión alternativo (si se configuró previamente")
            print ("Use otra cuenta de administrador en la misma PC")
        else:
            pregunta3=("MI COMPUTADORA ESTÁ TERRIBLEMENTE LENTA. ¿CÓMO REINSTALO WINDOWS 10?")
            respuesta=PreguntaRepetida (pregunta3)
            if respuesta == "si":
                print ("Copia de seguridad de la PC (si es posible")
                print ("Restablezca la PC desde Windows o las herramientas de recuperación")
                print ("Reinstale Windows desde una memoria USB si lo anterior no funciona")
            else:
                pregunta4=("¿POR QUÉ DESAPARECEN TODOS LOS ICONOS EN MI ESCRITORIO DE WINDOWS?")
                respuesta=PreguntaRepetida (pregunta4)
                if respuesta == "si":
                    print ("Haga clic derecho en el escritorio, seleccione Ver y luego Mostrar iconos del escritorio")
                    print ("Busque los iconos que faltan en la Papelera de reciclaje")
                    print ("Cree un nuevo acceso directo arrastrándolo desde el menú Inicio")
                else:
                    pregunta5=("WINDOWS NO ABRIRÁ UN ARCHIVO PORQUE NO TIENE UNA APLICACIÓN ASOCIADA CON ÉL. ¿QUÉ DEBO HACER?")
                    respuesta=PreguntaRepetida (pregunta5)
                    
                    if respuesta == "si":
                        print ("Seleccione las propiedades del archivo para identificar el tipo de archivo")
                        print ("Haga clic con el botón derecho en el archivo y elija Abrir con para encontrar la aplicación correspondiente")
                        print ("O use la configuración de la aplicación predeterminada de Windows")

                    else:
                        pregunta6=("¿POR QUÉ FALTA EL CUADRO DE BÚSQUEDA DE WINDOWS 10?")
                        respuesta=PreguntaRepetida (pregunta6)

                        if respuesta == "si":
                            print ("Accede a las opciones de búsqueda haciendo clic derecho en la barra de tareas")
                            print ("Elige si quieres recuperar la barra completa o solo un icono de búsqueda")
                        else:
                            pregunta7=("CÓMO ME LIBRO DE LA TERRIBLE CORTANA?")
                            respuesta=PreguntaRepetida (pregunta7)

                            if respuesta == "si":
                                print ("Deshabilite Cortana desde la configuración de Permisos de Cortana")
                                print ("Eliminar el botón de Cortana de la barra de tareas de Windows")
                                print ("Instale la aplicación gratuita Alexa si desea un reemplazo que valga la pena")

                            else:
                                pregunta8=("NO CREO QUE MI PC SE HA ACTUALIZADO A LA ÚLTIMA VERSIÓN DE WINDOWS. ¿CÓMO LO FORZO A HACERLO?")
                                respuesta=PreguntaRepetida (pregunta8)

                                if respuesta == "si":
                                    print ("Consulte la pantalla Acerca de su PC para averiguar en qué versión está")
                                    print ("Visite el sitio de Microsoft para averiguar cuál es la última versión")
                                    print ("Use la pantalla Buscar actualizaciones para descargar nuevas actualizaciones")

                                else:
                                    pregunta9=("MI PC CON WINDOWS 7 SIGUE PARPADEAR CON ADVERTENCIAS DE QUE EL SOPORTE HA TERMINADO. ¿QUÉ SIGNIFICA ESO?")
                                    respuesta=PreguntaRepetida (pregunta9)

                                    if respuesta == "si":
                                        print ("Busque el software de seguridad de Windows 7")
                                        print ("Actualizar a Windows 10")
                                        print ("Reemplace Windows 7 con CloudReady o un sistema operativo Linux")
                                    else:
                                        respuesta=repetirespañol ()
                                        if respuesta == "si":
                                            respuesta=0
                                            while respuesta != "portatil" and respuesta != "perifericos" and respuesta != "sobremesa" and respuesta != "pantalla":
                                                print (" Opciones:")
                                                print ("  - portatil")
                                                print ("  - perifericos")
                                                print ("  - sobremesa")
                                                print ("  - pantalla")
                                                respuesta = input ("Elige una: ")
                                            print ("")
                                            espanyol1 (respuesta)
                                            return respuesta

def perifericos_es () :
    def PreguntaRepetida (arg):
        respuesta=0
        while respuesta != "si" and respuesta != "no":
            respuesta = input (arg)
        print ("")
        return respuesta

    pregunta1=("¿POR QUÉ MI RATÓN NO FUNCIONA?")
    respuesta = PreguntaRepetida (pregunta1)
    if respuesta == "si":
        print ("Prueba diferentes puertos USB")
        print ("Use las teclas del mouse de Windows para ayudarlo a diagnosticar fallas")
        print ("Asegúrese de que las baterías estén cargadas")
    else:
        pregunta2=("¿POR QUÉ MI COMPUTADORA NO PUEDE VER MI IMPRESORA?")
        respuesta=PreguntaRepetida (pregunta2)
        if respuesta == "si":
            print ("Verifique que la impresora y la computadora estén en la misma banda inalámbrica")
            print ("Establecer la impresora como impresora predeterminada en Windows/Mac")
            print ("Ejecute el solucionador de problemas de la impresora")  
        else:
            respuesta=repetirespañol ()
            if respuesta == "si":
                respuesta=0
                while respuesta != "portatil" and respuesta != "sobremesa" and respuesta != "windows" and respuesta != "pantalla":
                    print (" Opciones:")
                    print ("  - portatil")
                    print ("  - sobremesa")
                    print ("  - windows")
                    print ("  - pantalla")
                    respuesta = input ("Elige una: ")
                print ("")
                espanyol1 (respuesta)
                return respuesta
  
def espanyol ():
    respuesta=0
    while respuesta != "portatil" and respuesta != "perifericos" and respuesta != "sobremesa" and respuesta != "windows" and respuesta != "pantalla":
        print (" Opciones:")
        print ("  - portatil")
        print ("  - perifericos")
        print ("  - sobremesa")
        print ("  - windows")
        print ("  - pantalla")
        respuesta = input ("Elige una: ")
    print ("")
    espanyol1 (respuesta)
    return respuesta

def espanyol1 (respuesta) :
    if respuesta == "portatil" :
        portatil_es ()
    if respuesta == "perifericos" :
        perifericos_es ()
    if respuesta == "sobremesa" :
        sobremesa_es ()
    if respuesta == "windows" :
        windows_es ()
    if respuesta == "pantalla" :
        pantalla_es ()

def ingles ():
    respuesta=0
    while respuesta != "laptop" and respuesta != "peripherals" and respuesta != "desktop" and respuesta != "windows" and respuesta != "screen":
        print (" Options:")
        print ("  - laptop")
        print ("  - peripherals")
        print ("  - desktop")
        print ("  - windows")
        print ("  - screen")
        respuesta = input ("Select one: ")
    print ("")
    ingles1 (respuesta)
    return respuesta

def ingles1 (respuesta) :
    if respuesta == "laptop" :
        laptop_ing ()
    if respuesta == "peripherals" :
        peripherals_ing ()
    if respuesta == "desktop" :
        desktop_ing ()
    if respuesta == "windows" :
        windows_ing ()
    if respuesta == "screen" :
        screen_ing ()

def idioma () :
    respuestaidioma=0
    while respuestaidioma != "espanyol" and respuestaidioma != "ingles":
        print ("Idiomas actualmente disponibles:")
        print (" - espanyol")
        print (" - ingles")
        respuestaidioma = input ("Elige uno de los dos: ")

    if respuestaidioma == "espanyol":
        espanyol ()
    if respuestaidioma == "ingles" :
        ingles ()

idioma ()
