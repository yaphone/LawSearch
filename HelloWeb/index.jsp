<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

	<!DOCTYPE html>
	<html lang="en">
	<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>秦皇岛市公安边防支队法律查询系统</title>

	<!-- Bootstrap -->
	<link href="css/bootstrap.css" rel="stylesheet">

	<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
	<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
	<!--[if lt IE 9]>
	      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
	      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
	    <![endif]-->
	    <script type="text/javascript" src="jquery/jquery.min.js"></script>
	<script type="text/javascript">
	//  $(document).ready(function(){                   //jquery ajax向服务器发送请求
	//  	$("#button").click(function(){
	//	  $("#textarea").load("LawServlet?law_file_name=" + $("#select_k1").text() + "&key_words=" + $("#keyWords").text());
	//  });
	//});
	 $(document).ready(function(){                   //jquery ajax向服务器发送请求
	  	$("#button").click(function(){
	  	var law_file_name = $("#select_k1").find("option:selected").text();
	  	var key_words = $("#keyWords").val();
	//  	alert(law_file_name + key_words);
	//  	  $("textarea").load("LawServlet", {"law_file_name":"test", "key_words":"打架"});
	  	  $("#textarea").load("LawServlet?law_file_name=" + law_file_name + "&key_words=" + key_words);
	  });
	}); 
 
	</script>
	</head>
	<body>

	<div class="row">
	  <div class="text-center col-md-6 col-md-offset-3" style="background:blue">
	      <h4>&nbsp;</h4>
	  </div>
	</div>
  
	<div class="container-fluid">
	  <div class="row">
	    <div class="col-md-6 col-md-offset-3">
	      <h1 align="center" class="text-center" style="font-size:20px"><img src="image/logo.png" width="42" height="43"></h1>

	      <h1 align="center" class="text-center" style="color:blue; font-size:20px;">秦皇岛市公安边防支队常用法律查询系统 </h1>
	    </div>
	  </div>
  
	</div>

	<div class="container">
	<form role="form">
	  <div class="form-group">
	      <label for="name">请选择法律文件：</label>
	      <select id="select_k1" class="form-control">
	         <option value="中华人民共和国治安管理处罚法" >中华人民共和国治安管理处罚法</option>
			<option value="河北省沿海船舶边防治安管理条例">河北省沿海船舶边防治安管理条例</option>
			<option value="河北省沿海船舶边防治安管理条例处罚裁量标准">河北省沿海船舶边防治安管理条例处罚裁量标准</option>
			<option value="办理刑事案件程序规定">办理刑事案件程序规定</option>
			<option value="道路交通安全法">道路交通安全法</option>
			<option value="公安机关人民警察执法过错责任追究规定">公安机关人民警察执法过错责任追究规定</option>
			<option value="公安机关适用继续盘问规定">公安机关适用继续盘问规定</option>
			<option value="禁毒法">禁毒法</option>
			<option value="人民警察使用警械和武器条例">办理刑事案件程序规定</option>
			<option value="刑法">刑法</option>
			<option value="刑事诉讼法">刑事诉讼法</option>      </select>
	   </div>
	</form>

	<form role="form">
	  <div class="form-group">
	    <label for="name">请输入关键字：</label>
	    <input id="keyWords" type="text" class="form-control" placeholder="文本输入">
	  </div>
	 </form>
	  <div align="right">
	    <button type="submit" id="button" class="btn btn-primary btn-lg btn-block"> 查询</button>
	  </div>
  
	 <form role="form">
	  <div class="form-group">
	    <label for="name">查询结果：</label>
	    <textarea id="textarea" class="form-control" rows="15" style="background:grey;color:yellow"></textarea>
	  </div>
	</form>

	  <div class="row">
	    <div class="text-center col-md-6 col-md-offset-3" style="background:blue">
	      <h4 align="center" style="color:white;">程序制作：中国有我一定黄 QQ：763665453</h4>
	    </div>
	  </div>
	  <hr>
	</div>
	<!-- jQuery (necessary for Bootstrap's JavaScript plugins) --> 
	<script src="js/jquery-1.11.2.min.js"></script>

	<!-- Include all compiled plugins (below), or include individual files as needed --> 
	<script src="js/bootstrap.js"></script>
	</body>
	</html>
	