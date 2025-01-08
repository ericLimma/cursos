<?php
class Calculadora
{
        public $a = 10;
        public $b = 7;
        public $operador = 'soma';

        public function calcular()
        {
                if ($this->operador == 'soma') {
                          // Corrigido
                        return $this->exibirCalculo(). ' = ' . ($this->a + $this->b);
                }
                return false;
        }

        public function exibirCalculo()
        {
                return "{$this->a} + {$this->b}";  // Corrigido
        }
}
$calcular = new Calculadora();
echo $calcular->calcular();
