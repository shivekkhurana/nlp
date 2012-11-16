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
}
.myButton:hover {
	background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #dfdfdf), color-stop(1, #ededed) );
	background:-moz-linear-gradient( center top, #dfdfdf 5%, #ededed 100% );
	filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#dfdfdf', endColorstr='#ededed');
	background-color:#dfdfdf;
}
.myButton:active {
	position:relative;
	top:1px;
}
ul li{

	list-style:none;
}
table{margin:0;padding:0;}
ul,table{

	border-top:2px solid #eee;
	padding:20px;
	color:#333;
	text-align: left;
	width:400px;
	margin:20px auto;
}
table{text-align: center;}
input[type="text"]{
	border:2px solid #a1dde5;
	outline:none;
}

input[type="text"]:focus{
	border:2px solid #3ab;
}


		</style>
	</head>
	<div class="container">
	<div class="Ohno"><span class="red">!</span><br/><h3>SPELL CHECKER</h3></div>
		<form action="/correct" method="post">
	 		<input type="text" id="observation" name="observation"></input>
	 		<br>
	 		<input type="submit" value="correct" class="myButton">
		</form>
		<h4>Optimal Correction(s)</h4>	
		<ul id="corrections">
						
				%for c in corrections:
    			<li>{{c}}</li>
  				%end
  			
		</ul>
		<table id="suggestions">
			<tr>
				<h4>All Suggestions</h4>
			</tr>
			<tr>
				<th>
					Word
				</th>
				<th>
					Levenstein Edit Distance
				</th>
			</tr>
			%for k,v in suggestions.items():
			<tr>
				<td>
					{{k}}
				</td>
				<td>
					{{v}}
				</td>
			</tr>
			%end
		</table>
	</div>
</html>