<?php
header('Content-Type: application/json');
$postData = file_get_contents('php://input');
$request = json_decode($postData, true);

$response = [
    'userInput' => $request['userInput']
];

echo json_encode($response);
?>
