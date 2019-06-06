<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="res/styles.css">
    <title>Consumo Api PokéAPI</title>
</head>
<body>
    <div class="container">
        <h2>Consumo Api PokéAPI: https://pokeapi.co/docs/v2/ </h2>
        <form method="get" id="form">
            <input type="text" placeholder="Ingrese 'pokemon', 'tipo' o 'generacion'." name="uri" >
            <button type="submit">Enviar</button>
        </form>
        <span><strong>Ejemplo: </strong>pokemon</span>

        <div class="content" id="content"></div>
    </div>

    <script src="res/app.js"></script>
</body>
</html>