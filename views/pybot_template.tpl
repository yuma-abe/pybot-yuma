<html>
<body bgcolor="#deefe1">
<h1 style="background:#3D8253;padding: 0.5em;margin:30px 0px 15px;color: white;">pybot</h1>
<form method="post" action="/hello" enctype="multipart/form-data">
メッセージを入力してください: <input type="text" name="input_text"><br>
<p>※例①：「気温データ　地名」と入力するとその地の平均気温を表示</p>
<p>※例②：「文字」と入力し、読み込みたい画像をアップロードすると手書きの数字を予想</p>
画像を選択してください: <input type="file" name="input_image"><br>
<input type="submit" value="送信">
</form>
<ul style="color: #1e366a;border: dotted #1e366a 1px;padding: 0.5em 0.5em 0.5em 2em;">
<li>入力されたメッセージ: {{input_text}}</li>
<li>pybotからの応答メッセージ: {{!output_text}}</li>
</ul>
</body>
</html>
