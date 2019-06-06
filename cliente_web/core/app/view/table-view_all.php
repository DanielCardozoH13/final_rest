<h2><?php echo ($data[1]);?></h2>
<table border="1">
    <thead>
        <th>Id</th>
        <th>Nombre</th>
        <th>Url</th>
    </thead>

    <tbody>
        <?php 
            $i=0;
            foreach($data[0]->results as $k => $v):?>
            <tr>
                <td><?=$i;$i=$i+1;?></td>
                <td><?=$data[0]->results[$k]->name;?></td>
                <td><?=$data[0]->results[$k]->url;?></td>
            </tr>
        <?php endforeach;?>
    </tbody>
</table>