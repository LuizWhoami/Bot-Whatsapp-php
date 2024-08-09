<?php

$servidor = 'localhost';
$usuario = 'root';
$senha = '';
$banco = 'bot_chat';
$conn = mysqli_connect($servidor, $usuario, $senha, $banco);

if($conn){
    ###echo 'tudo certo';
}else{
    #echo 'erro';
}

###variavel
$contato_final = $_GET['telefone'];
$msg = $_GET['msg'];
$usuario = $_GET['usuario'];

#echo "*telefone* $contato_final *msg* $msg *usuario* $usuario";


#verificar
$sql = "SELECT * FROM usuario WHERE telefone = '$contato_final'";
$query = mysqli_query($conn, $sql);
$total = mysqli_num_rows($query);

#consulta no banco
while($rows_usuarios = mysqli_fetch_array($query)){
    #irá verificar
    $status = $rows_usuarios['status'];
}

?>

<?php
#mensagem

$men2 = "*-- Barbearia-LS --* \n *Vai querer cortar cabelo, barba ou sobrancelha?* ";

$men3 = "*-- LS --* \n
*qual o dia e horario?* ";

$men4 = '*muito obrigado pela preferencia*';

$men5 = "*---PIX----*\n
Chave: (75) 99162-7153"
?>

<?php
#se for 0 ele vai cadastrar
if($total == 0){

$sql = "INSERT INTO usuario (telefone,status) VALUES ('$contato_final', '1')";
$query = mysqli_query($conn,$sql);
if($query){
echo '*Bem Vindo A Barbearia-LS*';
}
}#($total == 0){
?>


<?php

#se for 1 já é cliente
if($total == 1){


if($status == 1){

$resposta = $men2;
}

if($status == 2){
$resposta = $men3;
}

if($status == 3){
$resposta = $men4;
}

if($status == 4){
$resposta = $men5;
}


if($status < 5){

echo $resposta;

$status2 = $status + 1 ;
$sql = "UPDATE usuario SET status = '$status2' WHERE telefone = '$contato_final'";
$query = mysqli_query($conn, $sql);
}

if($status >= 6){
    
    echo "*Muito obrigado, pela preferencia* \n
    *AGUARDE O PIX* ";
    
    $status2 = $status + 1;
    $sql = "UPDATE usuario SET status = '1' WHERE telefone = '$contato_final'";
    $query = mysqli_query($conn, $sql);

####historico

$data = date('d-m=Y');
$sql = "INSERT INTO historico (telefone,msg_cliente,msg_bot,data) VALUES ('$contato_final', '$msg', '$resposta', '$data')";
$query = mysqli_query($conn,$sql);
}
}
?>
