<template>
	<div>
		<table class="table">
			<thead>
				<tr>
					<th>#</th>
					<th>1</th>
					<th>2</th>
					<th>3</th>
					<th>4</th>
					<th>5</th>
					<th>6</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="(item,index) in ta">{{item}}
					<td>{{index}}</td>
					<td>{{index+1}}</td>
					<td>{{index+2}}</td>
					<td>{{index+3}}</td>
					<td>{{index+4}}</td>
					<td>{{index+5}}</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>
<script>
export default{
	name:"dataTable",
	props:{ta:{type:Array}}
}
</script>
<style scoped>
</style>