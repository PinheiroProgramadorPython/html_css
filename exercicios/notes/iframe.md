# Iframes
###### iframes tem por padrão width="300px" e height="150px", porem podem ser alterados na Css !
###### iframes vem com esse parametro padrão frameborder="0" se trocar o numero 0 para 1 constroi uma borda no iframe,<br> podendo ser alterado  e confiurado também na Css usando o parametro (border: 1 px solid black;)
###### o parametro src="" é onde se coloca  o link  a ser exibido no Iframe
###### <iframe O texto que se colocar aqui , vai aparecer para o usuario , caso o navegador ou o site não aceite aparecer no iframe!<br> Podemos Colocar um link para  osite nesse caso usando a tag a 
### Carregando Paginas no iframe
###### podemos carregar também no iframe conteudos de paginas  do nosso proprio site<br>colocando dentro do src="a refrencia que leva a sua pagina.html"
###### Podemos selecionar quais paginas vão aparecer no iframe, usando links com a tag<a <br>e direcionando target="nome do iframe" dentro da tag<a usando um parametro name="nome do iframe" dentro da tag<iframe no html
###### podemos usar o parametro srcdoc="" dentro da tag<iframe para criar conteudo html dentro do iframe
### Segurança nos iframes
###### Para segurança do nosso site, devemos usar alguns parametros de segurança dentro da tag<iframe <br>use os parametros sandbox="sandbox" e referrerpolicy="no-referer"  para bloquear todas as ações dentro do iframe
###### podemos usar outros parametros para permitir algumas ações: sandbox="allow-same-origin allow-forms allow-scripts"
