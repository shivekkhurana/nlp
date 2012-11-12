<!doctype html>
<html>
	<head>
		<style type="text/css">
					body {
  font-family: 'Lucida Grande', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  font-size: 13px;
}

div.Ohno {
  background: #fff;
  margin: 0 auto;
  width: 300px;
  padding: 10px;
  text-align: center;
  font-weight:bold;
  color:#333;
  border:1px dotted #d8d8d8;
  
}

.red
{
  color:#ff0000;  
}
.container{
	text-align:center;
	max-width:600px;
	margin:100px auto;
}
.container input[type="text"]
{
  margin:40px auto;
  padding:10px 15px ;
  width:320px;
  color:#888;
}

.myButton {
  -moz-box-shadow:inset 0px 1px 0px 0px #ffffff;
	-webkit-box-shadow:inset 0px 1px 0px 0px #ffffff;
	box-shadow:inset 0px 1px 0px 0px #ffffff;
	background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #ededed), color-stop(1, #dfdfdf) );
	background:-moz-linear-gradient( center top, #ededed 5%, #dfdfdf 100% );
	filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ededed', endColorstr='#dfdfdf');
	background-color:#ededed;
	-moz-border-radius:6px;
	-webkit-border-radius:6px;
	border-radius:6px;
	border:1px solid #dcdcdc;
	display:inline-block;
	color:#bd7171;
	font-family:arial;
	font-size:15px;
	font-weight:bold;
	padding:6px 24px;
	text-decoration:none;
	text-shadow:1px 1px 0px #ffffff;
}.myButton:hover {
	background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #dfdfdf), color-stop(1, #ededed) );
	background:-moz-linear-gradient( center top, #dfdfdf 5%, #ededed 100% );
	filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#dfdfdf', endColorstr='#ededed');
	background-color:#dfdfdf;
}.myButton:active {
	position:relative;
	top:1px;
}
ul li{

	list-style:none;
}
ul{

	border-top:1px dashed #999;
	padding-top:20px;
	color:#333;
	text-align: left;
	width:400px;
	margin:20px auto;
}

		</style>
	</head>
	<div class="container">
	<div class="Ohno">OH NO <span class="red">!</span><br/>NOT YOU AGAIN<br/><h3>SPELL CHECKER</h3></div>
		<form action="/correct" method="post">
	 		<input type="text" id="observation" name="observation"></input>
	 		<br>
	 		<input type="submit" value="correct" class="myButton">
		</form>

		<ul id="corrections">
			
				%for c in corrections:
    			<li>{{c}}</li>
  				%end
  			
		</ul>
	</div>
</html>