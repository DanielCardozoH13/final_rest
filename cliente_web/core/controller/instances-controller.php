<?php
    if(isset($_REQUEST['uri']) && !empty($_REQUEST['uri'])) {
        $request = strtolower ($_REQUEST['uri']);
        if($request == "tipo"){
        	$arg="type";
        	$data[1] = "Lista de Tipos Pokemon";
        }elseif ($request == "generacion"){
        	$arg="generation";
        	$data[1] = "Lista de Generaciones Pokemon";
        }else{
        	$arg="pokemon";
        	$data[1] = "Lista de Pokemones";
        }
        $vista='table-view_all.php'; 
        $url_server = 'https://pokeapi.co/api/v2/'.$arg;
    	$json = file_get_contents($url_server);
    	$data[0] = json_decode($json);
    	require_once '../app/view/'.$vista;
        
        
    }else {
        echo json_encode("Error");
    }
?>