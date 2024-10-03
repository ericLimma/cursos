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
        <section class="section">
            <h1>PHP - Manipulacao de Strings</h1>
            <?php
            $string = 'Dedico estas memórias póstumas ao primeiro verme que roer as frias carnes do meu cadáver';

            echo "String incial: $string <br>";
            $stringLower = strtolower($string);
            echo "strintolower(): $stringLower <br>";
            $stringUpper = strtoupper($string);
            echo "strtoupper(): $stringUpper <br>";
            $ucfirst = ucfirst($string);
            echo "ucfirst: $ucfirst <br>";
            $strlen = strlen($string);
            echo "strlen(): $strlen --quantidade de letras<br>";

            $strReplaced = str_replace('a', '@', $string);
            echo "str_replace('a', '@, string): $strReplaced --substitui a letra<br>";
            $substr = substr($string, 7, 5);
            echo "substr(): $substr --retorna parte da string";

            $numQuebrado = '122,50';
            echo "<br> $numQuebrado";
            $numQuebrado2 = str_replace(',', '.', $numQuebrado);
            echo "<br> $numQuebrado2";
            ?>

        </section>
        <section class="section">
            <h1>PHP - Funcoes nativas para matematica</h1>
            <?php
            $numero = 127.35;
            $numero2 = 81;
            echo '<hr>';
            echo ceil($numero) . '<br>';
            echo floor($numero) . '<br>';
            echo round($numero) . '<br>';

            echo rand(10, 50) . '<br>';
            echo getrandmax() . '<br>';
            echo sqrt($numero2);


            ?>

        </section>
        <section class="section">
            <h1>PHP - Funcoes nativas para datas</h1>
            <?php
            $diaSemana = date('L');

            switch ($diaSemana) {
                case 1:
                    $diaSemana = "Domingo";
                    break;
                case 2:
                    $diaSemana = "Segunda-Feira";
                    break;
                case 3:
                    $diaSemana = "Terça-Feira";
                    break;
                case 4:
                    $diaSemana = "Quarta-Feira";
                    break;
                case 5:
                    $diaSemana = "Quinta-Feira";
                    break;
                case 6:
                    $diaSemana = "Sexta-Feira";
                    break;
                case 7:
                    $diaSemana = "Sábado";
                    break;
            }
            echo $diaSemana . '<br>';
            echo 'Hoje: ' . date('d / m / Y H:i') . '<br>';

            $data_inicial = '2024-09-21';
            $data_final = '2024-12-11';

            $time_inicial = strtotime($data_inicial);
            echo "$data_inicial - $time_inicial <br>";

            $time_final = strtotime($data_final);
            echo "$data_final - $time_final <br>";

            $diferenca_times = $time_final - $time_inicial;
            echo "$diferenca_times <br>";

            $diferenca_times = abs($time_inicial - $time_final);
            echo "$diferenca_times <br>";

            $segundos_dia = 24 * 60 * 60;
            echo "$segundos_dia <br>";

            echo $diferenca_times / $segundos_dia




            ?>

        </section>

    </main>
</body>

</html>