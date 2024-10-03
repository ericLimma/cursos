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
        <h1>PHP - Exercicio 1</h1>
        <section class="section">
            <?php
            function calcularIR($salario)
            {
                if ($salario  <= 1903.98) {
                    return 'Isento nessa faixa salarial';
                }
                if ($salario >= 1903.99 && $salario <= 2826.65) {
                    return $salario * 7.5 / 100;
                }
                if ($salario >= 2826.66 && $salario <= 3751.05) {
                    return $salario * 15 / 100;
                }
                if ($salario >= 3751.06 && $salario <= 4664.68) {
                    return $salario *22.5 / 100;
                }
                if ($salario > 4664.69) {
                    return $salario * 27.5 / 100;
                }
                return 'Informe um sálaruio válido';
            }
            echo calcularIR(1900);
            echo '<br>';
            echo calcularIR(2500);
            echo '<br>';
            echo calcularIR(3100);
            echo '<br>';
            echo calcularIR(4500);
            echo '<br>';
            echo calcularIR(5000);
            echo '<br>';
            ?>

        </section>

    </main>
</body>

</html>