// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import toolbar from './components/toolbar'
import dataTable from './components/table.vue'
import BootstrapVue from 'bootstrap-vue'
import router from './router/index.js'
Vue.config.productionTip = false
// Vue.use(BootstrapVue)
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'
/* eslint-disable no-new */
// Vue.component("add-minus",{
// 	template:"<div><button @click='add'>+</button><slot></slot><button @click='add'>增加</button><button @click.ctrl='show'>show</button></div>",
// 	data(){
// 		return{
// 			count:5
// 		}
// 	},
// 	methods:{
// 		add(){this.$parent._data.count++},
// 		show(){
// 			alert(this.$parent._data.count)
// 			show.$destory();
// 		}
// 		// minus(){this.$emit('haha')}
// 	}
// })
var newTemplate = Vue.extend({
	template:"<div><button @click='add'>+</button><slot></slot><button @click='add'>增加</button><button @click.ctrl='show'>show</button></div>",
	data(){
		return{
			count:5
		}
	},
	methods:{
		add(){this.$parent._data.count++},
		show(){
			alert(this.$parent._data.count)
		}
		// minus(){this.$emit('haha')}
	}
})
Vue.component("add-minus",newTemplate)
var add_test={
	name:"test",
	template:'<div><button v-on:click="sonadd">+</button><input type="text" v-model=\'zhi\'  :title=\'caled\'/></div>',
	props:['zhi'],
	methods:{
		sonadd(){
			// this.$parent.count1++;
			this.$emit('jia');
		},
		add(){
			alert("son");
		}
	},
	computed:{
		caled(){
			return this.zhi*2
		}
	}
}
let first = new Vue({
  el: '#app',
  components: {toolbar},
  data:{
  	newWord:"xxx公司",
  	count:0,
  	ctype:"toolbar"
  },
  router,
  methods:{
  	add(){
  		this.data.count++;
  	},
  	trans(){
  		this.ctype=this.ctype==="toolbar"?"p":"toolbar"
  	}
  },
  	mounted(){
		alert('mounted')
	},
	beforeUpdate(){
		console.log(this.count);
	}
})
var show = new Vue({
	el:"#tt",
	data:{
		result:["天津","北京","上海","重庆","太原","台北","哈尔滨","乌鲁木齐"],
		count1:10
	},
	components:{datatable:dataTable,test:add_test},
	methods:{
		add(e){
			console.log(e);
			this.count1++
		}
	},
	beforeCreate(){
		alert("beforeCreate")
	},
	created(){
		alert("created")
	},
	beforeMount(){
		alert('beforeMount')
	},
	mounted(){
		alert('mounted')
	}
})
