<?php
class Funcionario
{
        private static $idCounter = 0;

        public $id;
        public $nome;
        public $telefone;
        public $numFilhos;
        public $cargo = null;
        public $salrio = null;


        public function __construct($nome, $telefone, $numFilhos = 0)
        {
                $this->nome = ucfirst($nome);
                $this->telefone = $telefone;
                $this->numFilhos = $numFilhos;

                self::$idCounter++;
                $this->id = self::$idCounter;
        }

        function resumirCadFunc()
        {
                return "<hr>
                        Esse é o resumo do(a) cadastro do funcionário(a) {$this->nome}:<br>
                        Nome: {$this->nome}<br>
                        Telefone: {$this->telefone}<br>
                        Número de Filhos: {$this->numFilhos}<br>
                        ";
        }

        //getter setter(overloading)

        public function __set($atributo, $valor)
        {
                if (is_string($valor)) {
                        $valor = ucfirst($valor);
                }
                $this->$atributo = $valor;
        }
        public function __get($atributo)
        {
                return $this->$atributo;
        }


        /* function modificaNumFilhos($num)
        {
                $this->numFilhos += $num;
        }

        function setNome($nome)
        {
                $this->nome = $nome;
        }

        function setTelefone($telefone)
        {
                $this->telefone = $telefone;
        }
        function setNumFilhos($numFilhos)
        {
                $this->numFilhos = $numFilhos;
        }


        function getNome()
        {
                return $this->nome;
        }
        function getTelefone()
        {
                return $this->telefone;
        }
        function getNumFilhos()
        {
                return $this->numFilhos;
        } */

        public static function getIdCounter()
        {
                return self::$idCounter;
        }
}

$x = new Funcionario('joão', '19 9999-0000', 2);
echo $x->resumirCadFunc();
$x->__set('numFilhos', 5);
$x->__set('nome', "armando");
echo $x->resumirCadFunc();
$y = new Funcionario('luiza', '55 5555-5555');
echo $y->resumirCadFunc();
echo '<hr>';
echo $x->__get('nome');
echo '<hr>';
echo $y->__get('nome');
echo '<hr>';
echo Funcionario::getIdCounter();
