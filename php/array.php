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
            <h1>PHP - Arrays</h1>
            <?php
            $lista = ['laranja', 'maça', 'melão', 'melancia', 'uva'];
            echo '<pre>';
            print_r($lista);
            echo '</pre>';
            echo '<hr>';

            echo '<pre><code>';
            var_dump($lista);
            echo '</code></pre>';
            echo '<hr>';
            $lista[] = 'abacate';

            foreach ($lista as $fruta) {
                echo $fruta . '<br>';
            }

            if (in_array('abacate', $lista)) {
                echo 'Achou' . '<br>';
            } else {
                echo 'não achou' . '<br>';
            }

            echo array_search('uva', $lista) . '<br>';
            echo array_search('goiaba', $lista) . '<br>';


            ?>

        </section>

    </main>
</body>

</html>