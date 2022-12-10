 
 #Alvaro Escarti :))

 #Gracias por la ayudita
 #Team Pico y Pala 

 $Parameter1 = [String]$args[0]


 #Utilizo la variable args.Count para contar los argumentos que introduces
Write-Host "Has introducido : "$args.Count "argumentos" 

#Si hay un argumento, entramos dentro del if y en el siguiente if comprobamos que empieza por C:\,lo que quiere decir que es ruta absoluta
if ( $args.Count -eq 1 ){


    if ( $Parameter1.StartsWith("C:\") ) {

        Write-Host "La ruta: [ ** "$Parameter1 ** ] "Es absoluta"
        if ( Test-Path -Path $Parameter1 ){
            Write-Host "El fichero o directorio existe..."
        }else{
            Write-Host "No he encontrado nada..."
        }
    }else{
        Write-Host "La ruta:"$Parameter1 "NO Es absoluta"

    }


}


if ( $args.Count -eq 0 -or $args.Count -ge 2 ){

    Write-Host "Introduce un parametro valido"
 }

 #Sacar los permisos de un directorio o fichero 
 if ((Get-Acl -Path "$Parameter1").Access | Format-Table IdentityReference,FileSystemRights,AccessControlType,IsInherited,InheritanceFlags -AutoSize){
 
 Write-Host "Has introducido:"$Parameter1 "y sus permisos son: "
 #Vuelvo a poner el comando para que salga la informacion (ya que al hacerlo en un if no lo muestra, solo mi "echo")
 (Get-Acl -Path "$Parameter1").Access | Format-Table IdentityReference,FileSystemRights,AccessControlType,IsInherited,InheritanceFlags -AutoSize
 
 }
