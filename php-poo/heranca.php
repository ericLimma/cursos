<?php
class Veiculo
{
        public $placa;
        public $cor;
        function __construct($placa, $cor)
        {
                $this->placa = $placa;
                $this->cor = $cor;
        }

        function acelerar()
        {
                echo '<br> Acelerar;';
        }

        function freiar()
        {
                echo '<br> freiar';
        }

        function trocarMarcha()
        {
                echo '<br> Acionar embreagem com o pé e trocar marcha com a mão.';
        }
}
class Carro extends Veiculo
{

        public $teto_solar = true;

        function abrirTetoSolar()
        {
                echo '<br>Abrir teto solar;';
        }

        function alterarPosicaoVolante()
        {
                echo '<br>Alterar posicao volante;';
        }
}
class Moto extends Veiculo
{

        public $contra_peso_guidao = true;

        function empinar()
        {
                echo '<br> Empinar;';
        }

        function trocarMarcha()
        {
                echo '<br> Acionar embreagem com o mão e trocar marcha com a pé.';
        }
}
class Caminhao extends Veiculo {}



$carro = new Carro('ABC-1234', 'Vermelho');
$moto = new Moto('DEF-5678', 'Preto');
$caminhao = new Caminhao('GHI-9123', 'Branco');

printR($carro);
printR($moto);
printR($caminhao);

$carro->trocarMarcha();
$moto->trocarMarcha();

$caminhao->trocarMarcha();
