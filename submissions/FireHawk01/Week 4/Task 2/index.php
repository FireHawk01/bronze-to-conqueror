<?php
$name = $_GET['name'];
if (isset($name))
echo nl2br("We will call you shortly ".$name."\n");
?>



<html>
  <title>Login</title>
  <body>
  Book a new DTH connection
  <form name="MY Form"action="">
  Enter your name:<input type="text"name="name">
  <br>
  Mobile number:<input type="text"name="mobile">
  <br>
  <input type="submit"name="button1"value="Proceed">
  </form>
  </body>
</html>
