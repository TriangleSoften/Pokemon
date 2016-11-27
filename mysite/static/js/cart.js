
function calculatetotal(now, del, add) {
		var x = parseInt(now);
		var y = parseInt(add);
		var z = parseInt(del);
		document.getElementById("total1").innerHTML = "฿"+(x+y-z);
		document.getElementById("total1").value = x + y - z;
		}
function calculateShipping() {
		total1 = document.getElementById("total1").value;
		var x = 0;
		if (total1 < 1000) x = 100;
		if (total1 < 500) x = 150;
		document.getElementById("shipping").innerHTML = "฿"+x;
		document.getElementById("shipping").value = x;
		}
function calculatetotal2() {
		var total1 = document.getElementById("total1").value;
		var shipping = document.getElementById("shipping").value;
		document.getElementById("total2").innerHTML = "฿"+(total1 + shipping);
		document.getElementById("total2").value = total1 + shipping;
}
function calculateSubtotal(val,Pid,Pprice) {
	var x = parseInt(val);
	if(x>0){
		var now = document.getElementById("total1").value;
		if (now === undefined) now = 0;
		var name = new String(Pid);
		name = "subtotal"+name;
		var del = document.getElementById(name).value;
		if (del === undefined) del = 0;
		var add = x * Pprice;
		document.getElementById(name).innerHTML = "฿"+add;
		document.getElementById(name).value = add;
		calculatetotal(now, del, add);
		calculateShipping();
		calculatetotal2();
		
	}
}