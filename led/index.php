<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="aset/img/led.png">

    <title>LED switch berbasis web dengan bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="aset/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="sticky-footer.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <!-- Begin page content -->
    <div class="container">
      <div class="page-header">
        <h1>Nyalakan/Matikan LED</h1>
      </div>
		<?php
		if (isset($_POST['ON']))
		{
		exec("sudo python /home/samsul/gpio/led-on.py");
		}
		if (isset($_POST['OFF']))
		{
		exec("sudo python /home/samsul/gpio/led-off.py");
		}
		?>
		<form method="post">
		<button name="ON" class="btn btn-primary">Nyala</button>&nbsp;
		<button  name="OFF" class="btn btn-primary">Mati</button><br>
      		</form>
    </div>

    <footer class="footer">
      <div class="container">
        <p class="text-muted">@RTIKCilacap.</p>
      </div>
    </footer>

  </body>
</html>
