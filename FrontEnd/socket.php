<?php
function comm_Python($commands)
{
	// Create a TCP/IP socket.
	$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
	if ($socket === false) {
		return "Error 1: socket_create() failed: reason: " .
			socket_strerror(socket_last_error());
	}
	// Connect to the server running on the 'bot
	$result = socket_connect($socket, '54.186.237.252', 5006);
	if ($result === false) {
		return "Error 2: socket_connect() failed.\nReason: ($result) " .
			socket_strerror(socket_last_error($socket));
	}
	// Write two transmission, one of the size of the package,
	// and the second the package itself
	socket_write($socket, chr(strlen($commands)), 1);
	socket_write($socket, $commands, strlen($commands));

	// Get the response from the server - our current telemetry
	$resultLength = socket_read($socket, 1);
	if (strlen($resultLength) == 0) {
		return "Error 3: emptyness passed back from server";
	}
	else {
		$Telemetry = socket_read($socket, ord($resultLength));
	}
	socket_close($socket);
	return $Telemetry;
}

$message = array(
$_SERVER['SERVER_ADDR'],
"nuds"
);

echo comm_Python("nuds");
?>