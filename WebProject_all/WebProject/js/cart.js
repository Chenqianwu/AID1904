$(function (){
    //1.全选和取消全选
    var isChecked = false;//标记全选元素状态
    $(".checkAll").click(function (){
        isChecked = !isChecked;
        if(isChecked){
            //修改全选钮的显示图片
            $(".checkAll")
            .attr("src","../images/cart/product_true.png")
            //修改商品按钮的显示图片
            $(".checkItem")
            .attr("src","../images/cart/product_true.png")
            .attr("checked",true)
        }else{
            $(".checkAll")
            .attr("src","../images/cart/product_normal.png")
            $(".checkItem")
            .attr("src","../images/cart/product_normal.png")
            .attr("checked",false)
        }
        sum()
        /*
        //自定义标签属性或属性值
        $(this).prop("a","b").attr("aa","bb");
        console.log($(this).prop("a"));
        */
    })
    //2.反选
    $(".checkItem").click(function (){
        //2.1按钮自身状态及样式的修改
        //如果存在checked属性值,说明当前是选中,需要修改为未选中
        if($(this).attr("checked")){
            //修改标记同时修改显示图片
            $(this).attr("checked",false)
            .attr("src","../images/cart/product_normal.png");
        }else{
            $(this).attr("checked",true)
            .attr("src","../images/cart/product_true.png");
        }
        //2.2反选
        //获取被选中的商品数量 == 列表长度
        console.log($(".checkItem[checked=checked]").length);
        if($(".checkItem[checked=checked]").length == $(".checkItem").length){
            //修改全选按钮的图片和状态标记
            $(".checkAll")
            .attr("src","../images/cart/product_true.png");
            isChecked = true;
        }else{
            //修改全选按钮的图片和状态标记
            $(".checkAll")
            .attr("src","../images/cart/product_normal.png");
            isChecked = false;
        }
        sum()

    })
    //3.数量增减
    $(".add").click(function (){
        //获取输入框的值
        var value = $(this).prev().val();
        value++;
        $(this).prev().val(value);
        //价格联动
        changeSum($(this),value)
        sum()

    })
    $(".minus").click(function (){
        var value = $(this).next().val();
        if(value > 1){
            value--;
        }
        $(this).next().val(value)
        changeSum($(this),value)
        sum()
    })
    //4.价格联动
    function changeSum(that,n){
        //获取单价
        var s1 = that.parent().prev().find("p").html();
        //var s2 = that.parents(".item").find(".price p").html();
        //console.log(s1,s2);//$299.00
        var price = s1.substring(1)//299.00
        var tolPrice = price * n;
        tolPrice = tolPrice.toFixed(2);
        //console.log(tolPrice);
        //显示总金额
        that.parents(".item").find(".sum").html("¥"+tolPrice);

    }
    //5.移除商品
    $(".item .action").click(function (){
        $(this).parent().remove();
        sum()
    })
    //6.获取总数量和总价格
    function sum(){
        var num = 0;//总数量
        var price = 0;//总价格
        //获取被选中商品的总数量和总金额进行累加
        $(".checkItem[checked=checked]").each(function (){
            num += Number($(this).parents(".item").find(".count input").val());
            var str = $(this).parents(".item").find(".sum").html();
            var s = Number(str.substring(1));
            price += s;
        })
        //修改显示
        $(".total_count").html(num);
        price = price.toFixed(2);
        $(".total_price").html(price+"元");
    }












})