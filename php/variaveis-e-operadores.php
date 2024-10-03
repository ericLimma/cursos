<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP</title>

    <!-- Google Fonts - Comfortaa -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300..700&display=swap" rel="stylesheet">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

    <script src="https://kit.fontawesome.com/0740295107.js" crossorigin="anonymous"></script>
    <link rel="shortcut icon" href="assets/favicon/favicon.png" type="image/x-icon">
    <link rel="stylesheet" href="assets/css/styles.css">

</head>

<body>
    <main class="main">
        <h1>PHP - Variaveis e concatenação</h1>
        <section class="section">
            <?php
            $nome = 'Ana';
            $cor = 'Amarelo';
            $idade = 29;
            $atividadePreferida = 'jogar videogame';

            echo "<p> Olá, meu nome é $nome, tenho $idade, minha cor preferida é $cor, e eu amo $atividadePreferida</p>";
            //constantes

            define('BD_URL', 'endereco_db_dev');
            define('BD_USUARIO', 'usuario_dev');
            define('BD_SENHA', 'senha_dev');

            print BD_URL;
            echo BD_USUARIO;
            echo BD_SENHA;
            ?>

        </section>
        <section class="section">
            <?php

            $sera = false;
            if (true) {
                echo 'SIM';
            } else {
                echo 'nao';
            }
            echo '<hr>';
            $numero = 1;

            if ($numero == 2) {
                echo 'Igual a 2';
            } else if ($numero > 2) {
                echo 'Maior que 2';
            } else if ($numero < 2) {
                echo 'Menor que 2';
            } else if ($numero != 2) {
                echo 'Diferente de 2';
            };

            echo '<hr>';
            //operadores ternarios, uma condição, com dois retornos possiveis

            echo $numero == 2 ?  'Igual a 2' :  'diferente de 2';
            echo '<br>';
            echo $numero > 2 ? 'maior que 2' : 'menor que 2';

            ?>
        </section>
    </main>
</body>

</html>