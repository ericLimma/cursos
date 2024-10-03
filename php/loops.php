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

        <?php
        /* 
        $num = 0;
        while ($num < 50) {
            $num++;

            if ($num % 5 == 0) {
                continue;
            }
            echo $num . '<br>';
        } */

        $registros = [
            ['titulo' => 'Titulo noticia 1', 'conteudo' => 'Conteudo da notícia 1'],
            ['titulo' => 'Titulo noticia 2', 'conteudo' => 'Conteudo da notícia 2'],
            ['titulo' => 'Titulo noticia 3', 'conteudo' => 'Conteudo da notícia 3'],
            ['titulo' => 'Titulo noticia 4', 'conteudo' => 'Conteudo da notícia 4']
        ];

        /*         $idx = 0;

        while ($idx < count($registros)) {
            echo "<h3>" . $registros[$idx]['titulo'] . "</h3>";
            echo "<p>" . $registros[$idx]['conteudo'] . "</p>";
            $idx++;
        } */

        echo "<hr/>";

        for ($idx = 0; $idx < count($registros); $idx++) {
            echo "<h3>" . $registros[$idx]['titulo'] . "</h3>";
            echo "<p>" . $registros[$idx]['conteudo'] . "</p>";
        };

        $lista = ['cama', 'sofá', 'mesa', 'cadeira', 'fogão'];

        foreach ($lista as $movel) {
            echo "<p> $movel </p>";
        }

        echo '<hr><hr>';

        $funcionarios = [
            ['nome' => 'João', 'salario' => 2500],
            ['nome' => 'Julia', 'salario' => 3000],
            ['nome' => 'Maria', 'salario' => 2200]
        ];
        foreach ($funcionarios as $funcionario) {
            foreach ($funcionario as $idx => $valor) {
                echo "$idx - $valor, ";
            };
            echo '<hr>';
        };
        ?>

    </main>
</body>

</html>