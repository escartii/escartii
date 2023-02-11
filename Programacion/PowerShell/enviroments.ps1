#Alvaro Escarti :))


#Compruebo argumentos
if ( $args.Count -eq  1 ){
#Uso el comando SETX para crear variables de entorno
    SETX Escritorio "\Users\alvar\Desktop"

    Write-Host "La variable elegida es: Escritorio" 
    Write-Host "Puedes utilizar la variable para acceder desde cualquier sitio al Escritorio"
    Write-Host "La variable Escritorio la puedes utilizar con: env:Escritorio"

}

if ( $args.Count -eq 2 ){

    SETX SABERIP "ipconfig | find Dirección IPv4"
    Write-Host "La variable elegida es: SABERIP"
    Write-Host "La puedes utilizar para conocer tu IPv4"
    Write-Host "La variable SABERIP la puedes utilizar con: env:SABERIP"
    }

if ( $args.Count -eq 3 ){

    SETX eliminarUsuario "Net User usuario2 /delete"
    Write-Host -BackgroundColor DarkGreen "La variable elegida es: eliminarUsuario"
    Write-Host "Lo puedes usar para Borrar el usuario de tu hermano pequeño"
    Write-Host "La variable eliminarusuario la puedes utilizar con: env:eliminaruario"
}

if ( $args.Count -eq 4 ){

    SETX LOL "C:\Riot Games\League of Legends.exe"
    Write-Host -BackgroundColor DarkRed "La variable elegida es: LOL"
    Write-Host "Lo puedes utilizar para lanzar el cliente"
    Write-Host "La puedes utilizar así -> ""Env:LOL"
}

if ( $args.Count-eq 5 ){

    SETX Spotify "C:\Users\alvar\AppData\Local\Spotify.exe"
    Write-Host -BackgroundColor DarkGreen "La variable elegida es: Spotify"
    Write-Host "Lo puedes utilizar para lanzar rápidamente spotify"
    Write-Host "La puedes utilizar asi -> Env:Spotify"
}

if ( $args.Count -eq 0 -or $args.Count -ge 6 ){

    Write-Host " Debes Introducir 1 parametro como minimo y 5 como maximo"
 }
