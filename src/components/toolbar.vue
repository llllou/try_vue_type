<template>
	<div>
		<slot></slot>
		<slot name="sub-t"></slot>
		<ul>
			<li><button class="button">添加</button></li>
			<li><button class="button">修改</button></li>
			<li><button class="button">删除</button></li>
			<li><button class="button">附件</button></li>
			<li><a download="" :href="path">导出</a></li>
		</ul>
		<slot name="sub-t"></slot>
	</div>
</template>
<script>
export default{
	name:"toolbar",
	data(){
		return{
			path:"/uploader"
		}
	},
	created(){
		console.log("created")
	},
	beforeMounted(){
		console.log(this.data.path);
	},
	mounted(){
		console.log(this);
	}
}
</script>
<style scoped>
	ul{
		list-style: none;
	}
	ul li {
		float: left;
		margin: 0 10px;
	}
	button{
		padding: 5px 10px;
		color: white;
		font-weight: bold;
		background-color: #6cf;
		border: none;
	}
	a{
		display: block;
		padding: 5px 10px;
		color: white;
		background-color: #4ca;
		text-decoration:none;
		font-weight: bold;
	}
</style>