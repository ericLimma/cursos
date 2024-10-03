<?php
session_start();
$usuarioId = null;
$usuarioPerfilId = null;
$userName = null;
$usuarioAutenticado = false; // Definir a variável antes do loop
$perfis = [1 => 'Administrativo', 2 => 'Usuário'];

$usuarios_app = [
    ['id' => 1, 'email' => 'ericlimma378@gmail.com', 'senha' => '1221', 'nome' => 'Erick', 'perfil-id' => 1],
    ['id' => 2, 'email' => 'adm@test.com', 'senha' => '1221', 'nome' => 'Administrador', 'perfil-id' => 1],
    ['id' => 3, 'email' => 'user@test.com', 'senha' => 'user123', 'nome' => 'Usuário', 'perfil-id' => 2],
    ['id' => 4, 'email' => 'tester@test.com', 'senha' => 'tester123', 'nome' => 'Testador', 'perfil-id' => 2]
];

foreach ($usuarios_app as $user) {
    // Verifica o email
    if ($user['email'] == $_POST['email']) {
        // Verifica a senha
        if ($user['senha'] == $_POST['senha']) {
            $usuarioAutenticado = true;
            $userName = $user['nome'];
            $usuarioId = $user['id'];
            $usuarioPerfilId = $user['perfil-id'];
            break;
        }
    }
}

if ($usuarioAutenticado) {
    $_SESSION['usuario-autenticado'] = 'SIM';
    $_SESSION['id'] = $usuarioId;
    $_SESSION['usuario'] = $userName;
    $_SESSION['perfil-id'] = $usuarioPerfilId;

    header('Location: ../../home.php');
    exit();
} else {
    $_SESSION['usuario-autenticado'] = 'NÃO';
    unset($_SESSION['usuario']);
    header('Location: ../../index.php?login=error');
    exit();
}
