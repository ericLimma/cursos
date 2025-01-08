<?php
function printR($x)
{
        echo '<hr> <pre>';
        print_r($x);
        echo '</pre>';
}
class Pai
{
        private $nome;
        protected $sobrenome;
        public $humor;
        public function __construct($nome, $sobrenome, $humor)
        {
                $this->nome = $nome;
                $this->sobrenome = $sobrenome;
                $this->humor = $humor;
        }
        public function __set($attr, $value)
        {
                $this->$attr = $value;
        }
        public function __get($attr)
        {
                return $this->$attr;
        }
}

class Filho extends Pai {}
$pai = new Pai('Jorge', 'Moreira', 'Feliz');
/* echo $pai->humor;
echo '<br>';

echo $pai->__get('nome');
echo '<br>';
echo $pai->__get('sobrenome');
 */
printR($pai);

$filho = new Filho('Gabriel', 'Felipe', 'bravo');
printR($filho);
