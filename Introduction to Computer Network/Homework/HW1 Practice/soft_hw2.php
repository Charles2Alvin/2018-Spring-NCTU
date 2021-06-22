<?php

try{
	$connect=new PDO("sqlite:hahahaemmm/wow.db");

	echo "Congratulations! Database already connected! :)<br>";
}
catch(PDOException $e)
{
    echo $e->getMessage();
}

if($_SERVER['REQUEST_METHOD'] == 'POST'){
	if($_POST['action'] == '添加'){
		$sth = $connect->prepare('INSERT INTO info (content) values (?)');
		$sth->execute(array($_POST['text']));

	}else if($_POST['action'] == '删掉'){
		$sth = $connect->prepare('DELETE FROM info where id = ?');
		if(isset($_POST['del'])){
			foreach($_POST['del'] as $i){
				$sth->execute(array($i));
			}
		}
	}

	header('Location:note.php');
	exit();
}
		
?>
	
<?php
echo "<h2>...Note Studio...</h2>";
echo "你可以在这里编辑你的笔记:)";
?>


<form method = "POST">
<textarea name = "text">
</textarea>
<br>
<input type = "submit" name = "action" value = "添加">
</form>

<table border = "1">
<tr><td>编号</td><td>内容</td><td>删掉</td></tr>

<?php
$sth = $connect->prepare('SELECT * FROM info');
$sth->execute();
while($row = $sth->fetch()){
	echo '<tr><td>';
	echo $row['id'];
	echo '</td><td>';
	echo $row['content'];
	echo '</td><td>';
	echo '<input type = "checkbox" name = "del[]" value = "'.$row['id'].'">';
	echo '</td><tr>';
}
?>
</table>
<input type = "submit" name = "action" value = "删掉">
</form>













