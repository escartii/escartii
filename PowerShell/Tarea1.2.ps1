 
 #Alvaro Escarti :))

 #Buenas Angel, he hecho los 3 ejercicios en un mismo script

 $Parameter1 = [String]$args[0]

 #Utilizo la variable args.Count para contar los argumentos que introduces
Write-Host "Has introducido : "$args.Count "argumentos" 


#Si hay un argumento entramos dentro del if, en el siguiente if comprobamos que NO empieza por C:\,lo que quiere decir que es ruta relativa
if ( $args.Count -eq 1 ){

    if (  $Parameter1.StartsWith(".\") -or $Parameter1.StartsWith("..\" )) {
        Write-Host "La ruta: [ ** $Parameter1 ** ] Es relativa"
        #IMPORTANTE !!
        #Comprobar si existe un directorio o fichero
        #Tienes que saber en que ruta te encuentras (pwd) para que encuentre el directorio o fichero que quieres
        if ( Test-Path -Path $Parameter1 ){
            Write-Host "El fichero o directorio existe..."
        }else{
            Write-Host "No he encontrado nada..."
        }
        
    }else{
        Write-Host "La ruta:"$Parameter1 "Es absoluta"
    }

}


if ( $args.Count -eq 0 -or $args.Count -ge 2 ){

    Write-Host "Introduce un parametro valido"
 }


 #Sacar los permisos de un directorio o fichero 
 (Get-Acl -Path $Parameter1).Access | Format-Table IdentityReference,FileSystemRights,AccessControlType,IsInherited,InheritanceFlags -AutoSize