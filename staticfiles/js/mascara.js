
$(function(){
    $('.mask-cpf').mask('000.000.000-00', {reverse: true});
    $('.mask-cnpj').mask('00.000.000/0000-00', {reverse: true});
    $('.mask-telefone').mask(' (00)00000-0000', {reverse: true});
    $('.mask-state').mask('AA', {reverse: true});
    $('.mask-cep').mask('00.000-000', {reverse: true});
    $('.mask-hora').mask('00:00', {reverse: true});
    $('.mask-perc').mask('00.00', {reverse: true});
});
