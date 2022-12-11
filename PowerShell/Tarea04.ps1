#Alvaro Escarti :))

$fichero = "sample.txt"
$Parameter1 = [String]$args[0]
$Parameter2 = [String]$args[1]
#Creo el argumento 3 por si el segundo argumento es "test"
$Parameter3 = [String]$args[2]
#He encontrado el comando findstr que funciona (find es demasiado complejo y siempre daba errores)
if ( $args.Count -le 1 -or $args.Count -gt 3 ){

    Write-Host "Debes introducir dos parametros de entrada"
 }
    
if ( $args.Count -eq 2 -or $args.Count -eq 3 ){
    #Compruebo si el usuario introducido como parametro 1 existe
    $existeUsuario = net user | findstr $Parameter1
    Write-Host "Has introducido dos parametros"
        if ( $existeUsuario ){
            Write-Host "El usuario introducido es: " $Parameter1 "Y EXISTE "
            if ( $Parameter2 -eq "replenish" ){
                #Voy a comprobar si existe la ruta para borrarla, si no sale un error como que ya está creada
                if ( Test-Path -Path C:\Users\$Parameter1 ){ 
                    Write-Host -BackgroundColor DarkGreen "La ruta existe, el usuario ha iniciado sesión alguna vez"
                    Write-Host
                    Write-Host "tu carpeta home es... C:\Users\$Parameter1"
                    #uso ea -0 para evitar errores, ya que si está creado va a aparecer un error
                    #(iba a borrar el home de ese usuario, pero si es un usuario relevante, no es del todo optimo)
                    #asi que prefiero hacerlo asi
                    Write-Host "Procedo a crear el directorio Workspace con sus subdirectorios"
                    mkdir -p C:\Users\$Parameter1\Workspace -ea 0
                    ForEach ($Dir in ("config", "bin", "source", "rsrc")){
                         #Creo los ficheros dentro de las carpetas
                         New-Item -ItemType Directory -Path C:\Users\$Parameter1\Workspace\$Dir -ea 0
                         New-Item -ItemType File C:\Users\$Parameter1\Workspace\config\sample.txt -ea 0
                         New-Item -ItemType File C:\Users\$Parameter1\Workspace\bin\sample.txt -ea 0
                         New-Item -ItemType File C:\Users\$Parameter1\Workspace\source\sample.txt -ea 0
                         New-Item -ItemType File C:\Users\$Parameter1\Workspace\rsrc\sample.txt -ea 0
                         
                    }
                }else{
                    Write-Host -BackgroundColor DarkRed "tu carpeta home no existe, existe el usuario pero nunca has iniciado sesión, procedo a crear tu home..."
                    mkdir -p C:\Users\$Parameter1\Workspace -ea 0
                    ForEach ($Dir in ("config", "bin", "source", "rsrc")){
                        New-Item -ItemType Directory -Path C:\Users\$Parameter1\Workspace\$Dir -ea 0
                        New-Item -ItemType Directory -Path C:\Users\$Parameter1\Workspace\$Dir -ea 0
                        New-Item -ItemType File C:\Users\$Parameter1\Workspace\config\sample.txt -ea 0
                        New-Item -ItemType File C:\Users\$Parameter1\Workspace\bin\sample.txt -ea 0
                        New-Item -ItemType File C:\Users\$Parameter1\Workspace\source\sample.txt -ea 0
                        New-Item -ItemType File C:\Users\$Parameter1\Workspace\rsrc\sample.txt -ea 0
                   }
                }
            }
       
      }else{
            Write-Host " [ ERROR ] The USER:"$Parameter1 "NOT EXISTS"
        }

}

#test

 #Compruebo que existe la RUTA indicada en el parametro 3
if ( $Parameter2 -eq "test" -and $Parameter3.StartsWith(".\") -or $Parameter3.StartsWith("..\") -or $Parameter3.StartsWith("C:\")) {
    Write-Host "Has introducido la palabra test y has indicado una ruta valida... ahora voy a comprobar si existe"

    if ( Test-Path -Path $Parameter3 ){
        Write-Host "La ruta existe"
        Write-Host "Voy a buscar que ficheros tienen permisos.."
        #Write-Host "Muestro los permisos de los ficheros"
        #Get-Childitem -path $Parameter3 -recurse -directory | ls
        Write-Host " " 
        #Compruebo si hay directorios en la ruta que introduces en el tercer argumento        
        Get-Childitem -path $Parameter3 -recurse -directory | ls | ForEach-Object {
        #Compruebo que ficheros tienen todos los permisos
        $encontrarpermisos = Get-Acl $_.FullName | findstr /i "fullcontrol"
            if ( $encontrarpermisos ){
                Write-Host -BackgroundColor DarkGreen "$encontrarpermisos"
            }
                    
       }
}else{
          
      Write-Host "La ruta no existe"
      }
}


 if ( $Parameter2 -eq "clean" ){
    if ( Test-Path -Path $Parameter3 ){
        Write-Host "La ruta existe"
        Write-Host "Procedo a borrar..."
        #Al final uso rm recursivamente para eliminar todo 
        #Cuidado con Ejecutarlo, deberia salirte un aviso de si realmente quieres borrarlo... 
        rm -Recurse -Force $Parameter3
     }

}
