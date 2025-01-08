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
    <link rel="shortcut icon" href="assets/favicon/php_logo.png" type="image/x-icon">
    <link rel="stylesheet" href="assets/css/styles.css">


</head>

<body>
    <main class="main">
        <h1>PHP - POO</h1>
        <h2>Pilar da Abstração</h2>
        <p>Como entendemos as caraccteristicas de um objeto e o transportamos para a programação.</p>
        <?php
        include('encapsulamento.php');
        ?>
        <hr>
        <?php
        include('heranca.php');
        ?>
        <hr>
        <?php
        include('Calculadora.php');
        ?>
        <hr>
        <?php
        include('abstracao.php');
        ?>
    </main>
</body>

</html>