var db = openDatabase("JAY", "1.0", "it's to save jay'songs data!", 1024 * 1024); 
	function initDatabase() {
		//初始化数据库
	    var db = getCurrentDb();
	    if(!db) {
	        alert("对不起，浏览器不支持");
	        return;
	    }    
	    db.transaction(function (trans) {
	        trans.executeSql("create table if not exists Movie(title text null,url text null)", [], function (trans, result) {
	            
	        }, function (trans, message) {
	            alert(message);
	        });
	    }, function (trans, result) {
	    }, function (trans, message) {
	    });
	}
	//创建数据库
		first.onclick =function(){
			//打开数据库，或者直接连接数据库参数：数据库名称，版本，概述，大小
			if(db!=""){
				alert("ok");
			}
			return db;
		}
second.onclick=function(){
		db.transaction(function (context) {
		context.executeSql('CREATE TABLE song (name VARCHAR,love INT)');
	}, function (error) {
		console.log('创建表失败:[' + error.message + ']');
	}, function () {
		console.log('创建表成功');
	});
		}
//往表里插入数据
		var a="说好不哭";
		var b="5461686"
		third.onclick=function(){
		db.transaction(function (context) {
		context.executeSql('INSERT INTO song (name,LOVE) VALUES (?,?)',[a,b]);//使用占位符的方法，再获取用户输入的信息即可
	}, function (error) {
		console.log('插入数据失败:[' + error.message + ']');
	}, function () {
		console.log('插入数据成功');
	});
		}
//往表里获取用户输入的数据
	insong.onclick=function(){
		var song = document.getElementById("inputsong").value;
		var love = document.getElementById("inputlove").value;
		db.transaction(function (context) {
			context.executeSql('INSERT INTO song (name,LOVE) VALUES (?,?)',[song,love]);//使用占位符的方法，再获取用户输入的信息即可
		}, function (error) {
			console.log('插入数据失败:[' + error.message + ']');
		}, function () {
			console.log('插入数据成功');
		});
	}
//查询数据库
	query.onclick=function(){
		  db.transaction(function (context) {
			context.executeSql('SELECT * FROM song', [], function (context, results) {
			var items = results.rows;
			for (i = 0; i < items.length; i++) {
				var item = items.item(i);
				var li=document.createElement('li');
				li.innerText=item.name;
				ul.append(li);
				console.log(li);
				// var t1=["t1","t2","t3"];
				// document.getElementById(t1[i]).innerText=item.name;	
			}
		
		});
	}, function (error) {
		console.log('查询数据失败:[' + error.message + ']');
	}, function () {
		console.log('查询数据成功');
	});
	}
