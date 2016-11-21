// brython.js www.brython.info
// version 1.1.20130307-204354
// version compiled from commented, indented source files at http://code.google.com/p/brython/
__BRYTHON__=new Object()
__BRYTHON__.__getattr__=function(attr){return this[attr]}
__BRYTHON__.date=function(){
if(arguments.length===0){return JSObject(new Date())}
else if(arguments.length===1){return JSObject(new Date(arguments[0]))}
else if(arguments.length===7){return JSObject(new Date(arguments[0],
arguments[1]-1,arguments[2],arguments[3],
arguments[4],arguments[5],arguments[6]))}
}
__BRYTHON__.has_local_storage=typeof(Storage)!=="undefined"
__BRYTHON__.has_json=typeof(JSON)!=="undefined"
__BRYTHON__.version_info=[1,1,"20130307-204354"]
__BRYTHON__.path=[]
function abs(obj){
if(isinstance(obj,int)){return int(Math.abs(obj))}
else if(isinstance(obj,float)){return float(Math.abs(obj.value))}
else{throw TypeError("Bad operand type for abs(): '"+str(obj.__class__)+"'")}
}
function $alert(src){alert(str(src))}
function all(iterable){
while(true){
try{
var elt=next(iterable)
if(!bool(elt)){return False}
}catch(err){return True}
}
}
function any(iterable){
if(iterable.__item__===undefined){
throw TypeError("'"+iterable.__class__.__name__+"' object is not iterable")
}
while(true){
try{
var elt=next(iterable)
if(bool(elt)){return True}
}catch(err){return False}
}
}
function assert_raises(){
var $ns=$MakeArgs('assert_raises',arguments,['exc','func'],{},'args','kw')
var args=$ns['args']
try{$ns['func'].apply(this,args)}
catch(err){
if(err.name!==$ns['exc']){
throw AssertionError(
"exception raised '"+err.name+"', expected '"+$ns['exc']+"'")
}
return
}
throw AssertionError("no exception raised, expected '"+$ns['exc']+"'")
}
function bool(obj){
if(obj===null){return False}
else if(obj===undefined){return False}
else if(isinstance(obj,dict)){return obj.keys.length>0}
else if(isinstance(obj,tuple)){return obj.items.length>0}
else if(typeof obj==="boolean"){return obj}
else if(typeof obj==="number" || typeof obj==="string"){
if(obj){return true}else{return false}
}else if('__bool__' in obj){return obj.__bool__()}
else if('__len__' in obj){return obj.__len__()>0}
return true
}
bool.__class__=$type
bool.__name__='bool'
bool.__str__=function(){return "<class 'bool'>"}
bool.toString=bool.__str__
bool.__hash__=function(){
if(this.valueOf())return 1
return 0
}
function $class(obj,info){
this.obj=obj
this.info=info
this.__class__=Object
this.toString=function(){return "<class '"+info+"'>"}
}
function $confirm(src){return confirm(src)}
function dict(){
if(arguments.length==0){return new $DictClass([],[])}
else if(arguments.length===1 && isinstance(arguments[0],dict)){
return arguments[0]
}
var $ns=$MakeArgs('dict',arguments,[],{},'args','kw')
var args=$ns['args']
var kw=$ns['kw']
if(args.length>0){
var iterable=args[0]
var obj=new $DictClass([],[])
for(var i=0;i<iterable.__len__();i++){
var elt=iterable.__item__(i)
obj.__setitem__(elt.__item__(0),elt.__item__(1))
}
return obj
}else if(kw.$keys.length>0){
return kw
}
}
dict.__class__=$type
dict.__name__='dict'
dict.toString=function(){return "<class 'dict'>"}
function $DictClass($keys,$values){
var x=null
var i=null
this.iter=null
this.__class__=dict
this.$keys=$keys 
this.$values=$values 
}
$DictClass.prototype.toString=function(){
if(this.$keys.length==0){return '{}'}
var res="{",key=null,value=null,i=null 
var qesc=new RegExp('"',"g")
for(var i=0;i<this.$keys.length;i++){
if(typeof this.$keys[i]==="string"){key='"'+$escape_dq(this.$keys[i])+'"'}
else{key=str(this.$keys[i])}
if(typeof this.$values[i]==="string"){value='"'+$escape_dq(this.$values[i])+'"'}
else{value=str(this.$values[i])}
res +=key+':'+value+','
}
return res.substr(0,res.length-1)+'}'
}
$DictClass.prototype.__add__=function(other){
var msg="unsupported operand types for +:'dict' and "
throw TypeError(msg+"'"+(str(other.__class__)|| typeof other)+"'")
}
$DictClass.prototype.__class__=dict
$DictClass.prototype.__contains__=function(item){
return this.$keys.__contains__(item)
}
$DictClass.prototype.__delitem__=function(arg){
for(var i=0;i<this.$keys.length;i++){
if(arg.__eq__(this.$keys[i])){
this.$keys.splice(i,1)
this.$values.splice(i,1)
return
}
}
throw KeyError(str(arg))
}
$DictClass.prototype.__eq__=function(other){
if(!isinstance(other,dict)){return False}
if(other.$keys.length!==this.$keys.length){return False}
for(var i=0;i<this.$keys.length;i++){
var key=this.$keys[i]
for(j=0;j<other.$keys.length;j++){
try{
if(other.$keys[j].__eq__(key)){
if(!other.$values[j].__eq__(this.$values[i])){
return False
}
}
}catch(err){void(0)}
}
}
return True
}
$DictClass.prototype.__getattr__=function(attr){
return $getattr(this,attr)
}
$DictClass.prototype.__getitem__=function(arg){
for(var i=0;i<this.$keys.length;i++){
if(arg.__eq__(this.$keys[i])){return this.$values[i]}
}
throw KeyError(str(arg))
}
$DictClass.prototype.__hash__=function(){throw TypeError("unhashable type: 'dict'");}
$DictClass.prototype.__in__=function(item){return item.__contains__(this)}
$DictClass.prototype.__item__=function(i){return this.$keys[i]}
$DictClass.prototype.__len__=function(){return this.$keys.length}
$DictClass.prototype.__ne__=function(other){return !this.__eq__(other)}
$DictClass.prototype.__next__=function(){
if(this.iter==null){this.iter==0}
if(this.iter<this.$keys.length){
this.iter++
return this.$keys[this.iter-1]
}else{
this.iter=null
throw StopIteration()
}
}
$DictClass.prototype.__not_in__=function(item){return !(item.__contains__(this))}
$DictClass.prototype.__setitem__=function(key,value){
for(var i=0;i<this.$keys.length;i++){
try{
if(key.__eq__(this.$keys[i])){
this.$values[i]=value
return
}
}catch(err){
void(0)
}
}
this.$keys.push(key)
this.$values.push(value)
}
$DictClass.prototype.items=function(){
return new $iterator(zip(this.$keys,this.$values),"dict_items")
}
$DictClass.prototype.keys=function(){
return new $iterator(this.$keys,"dict keys")
}
$DictClass.prototype.values=function(){
return new $iterator(this.$values,"dict values")
}
function dir(obj){
var res=[]
for(var attr in obj){res.push(attr)}
res.sort()
return res
}
function enumerate(iterator){
var res=[]
for(var i=0;i<iterator.__len__();i++){
res.push([i,iterator.__item__(i)])
}
return res
}
function $eval(src){
if(src===""){throw SyntaxError("unexpected EOF while parsing")}
try{return eval(__BRYTHON__.py2js(src).to_js())}
catch(err){
if(err.py_error===undefined){throw RuntimeError(err.message)}
if(document.$stderr){document.$stderr.__getattr__('write')(document.$stderr_buff+'\n')}
else{throw(err)}
}
}
function exec(src){
try{eval(__BRYTHON__.py2js(src).to_js())}
catch(err){
if(err.py_error===undefined){err=RuntimeError(err.message)}
var trace=err.__name__+': '+err.message+err.info
if(document.$stderr){document.$stderr.__getattr__('write')(trace)}
else{console.log(trace)}
throw err
}
}
function filter(){
if(arguments.length!=2){throw TypeError(
"filter expected 2 arguments, got "+arguments.length)}
var func=arguments[0],iterable=arguments[1]
var res=[]
for(var i=0;i<iterable.__len__();i++){
if(func(iterable.__item__(i))){
res.push(iterable.__item__(i))
}
}
return res
}
function float(value){
if(value===undefined){return new $FloatClass(0.0)}
if(typeof value=="number" ||(typeof value=="string" && !isNaN(value))){
return new $FloatClass(parseFloat(value))
}
if(isinstance(value,float))return value
if(value=='inf')return new $FloatClass(Infinity)
if(value=='-inf')return new $FloatClass(-Infinity)
if(typeof value=='string' && value.toLowerCase()=='nan')return new $FloatClass(Number.NaN)
throw ValueError("Could not convert to float(): '"+str(value)+"'")
}
float.__class__=$type
float.__name__='float'
float.toString=function(){return "<class 'float'>"}
float.__hash__=function(){
frexp=function(re){
var ex=Math.floor(Math.log(re)/ Math.log(2))+ 1
var frac=re / Math.pow(2, ex)
return[frac, ex]
}
if(this.value===Infinity || this.value===-Infinity){
if(this.value < 0.0)return -271828
return 314159
}else if(isNaN(this.value)){
return 0
}
var r=frexp(this.value)
r[0]*=Math.pow(2,31)
hipart=int(r[0])
r[0]=(r[0]- hipart)* Math.pow(2,31)
var x=hipart + int(r[0])+(r[1]<< 15)
return x & 0xFFFFFFFF
}
function $FloatClass(value){
this.value=value
this.__class__=float
this.__hash__=float.__hash__
}
$FloatClass.prototype.toString=function(){
var res=this.value+'' 
if(res.indexOf('.')==-1){res+='.0'}
return str(res)
}
$FloatClass.prototype.__class__=float
$FloatClass.prototype.__bool__=function(){return bool(this.value)}
$FloatClass.prototype.__floordiv__=function(other){
if(isinstance(other,int)){
if(other===0){throw ZeroDivisionError('division by zero')}
else{return float(Math.floor(this.value/other))}
}else if(isinstance(other,float)){
if(!other.value){throw ZeroDivisionError('division by zero')}
else{return float(Math.floor(this.value/other.value))}
}else{throw TypeError(
"unsupported operand type(s) for //: 'int' and '"+other.__class__+"'")
}
}
$FloatClass.prototype.__hash__=float.__hash__
$FloatClass.prototype.__in__=function(item){return item.__contains__(this)}
$FloatClass.prototype.__not_in__=function(item){return !(item.__contains__(this))}
$FloatClass.prototype.__truediv__=function(other){
if(isinstance(other,int)){
if(other===0){throw ZeroDivisionError('division by zero')}
else{return float(this.value/other)}
}else if(isinstance(other,float)){
if(!other.value){throw ZeroDivisionError('division by zero')}
else{return float(this.value/other.value)}
}else{throw TypeError(
"unsupported operand type(s) for //: 'int' and '"+other.__class__+"'")
}
}
var $op_func=function(other){
if(isinstance(other,int)){return float(this.value-other)}
else if(isinstance(other,float)){return float(this.value-other.value)}
else if(isinstance(other,bool)){
var bool_value=0;
if(other.valueOf())bool_value=1
return float(this.value-bool_value)}
else{throw TypeError(
"unsupported operand type(s) for -: "+this.value+" (float) and '"+other.__class__+"'")
}
}
$op_func +='' 
var $ops={'+':'add','-':'sub','*':'mul','%':'mod'}
for($op in $ops){
eval('$FloatClass.prototype.__'+$ops[$op]+'__ = '+$op_func.replace(/-/gm,$op))
}
var $comp_func=function(other){
if(isinstance(other,int)){return this.value > other.valueOf()}
else if(isinstance(other,float)){return this.value > other.value}
else{throw TypeError(
"unorderable types: "+this.__class__+'() > '+other.__class__+"()")
}
}
$comp_func +='' 
var $comps={'>':'gt','>=':'ge','<':'lt','<=':'le','==':'eq','!=':'ne'}
for($op in $comps){
eval("$FloatClass.prototype.__"+$comps[$op]+'__ = '+$comp_func.replace(/>/gm,$op))
}
var $notimplemented=function(other){
throw TypeError(
"unsupported operand types for OPERATOR: '"+this.__class__+"' and '"+other.__class__+"'")
}
$notimplemented +='' 
for($op in $operators){
var $opfunc='__'+$operators[$op]+'__'
if(!($opfunc in $FloatClass.prototype)){
eval('$FloatClass.prototype.'+$opfunc+"="+$notimplemented.replace(/OPERATOR/gm,$op))
}
}
function getattr(obj,attr,_default){
if(obj.__getattr__!==undefined &&
obj.__getattr__(attr)!==undefined){
return obj.__getattr__(attr)
}
else if(_default !==undefined){return _default}
else{throw AttributeError(
"'"+str(obj.__class__)+"' object has no attribute '"+attr+"'")}
}
function hasattr(obj,attr){
try{getattr(obj,attr);return True}
catch(err){return False}
}
function hash(obj){
if(isinstance(obj, int)){return obj.valueOf();}
if(isinstance(obj, bool)){return int(obj);}
if(obj.__hashvalue__ !==undefined){return obj.__hashvalue__;}
if(obj.__hash__ !==undefined){
obj.__hashvalue__=obj.__hash__()
return obj.__hashvalue__
}else{
throw AttributeError(
"'"+str(obj.__class__)+"' object has no attribute '__hash__'")
}
}
function input(src){
return prompt(src)
}
function int(value){
if(value===undefined){return 0}
else if(isinstance(value,int)){return value}
else if(value===True){return 1}
else if(value===False){return 0}
else if(typeof value=="number" ||
(typeof value=="string" && parseInt(value)!=NaN)){
return parseInt(value)
}else if(isinstance(value,float)){
return parseInt(value.value)
}else{throw ValueError(
"Invalid literal for int() with base 10: '"+str(value)+"'"+value.__class__)
}
}
int.__class__=$type
int.__name__='int'
int.toString=function(){return "<class 'int'>"}
Number.prototype.__class__=int
Number.prototype.__floordiv__=function(other){
if(isinstance(other,int)){
if(other==0){throw ZeroDivisionError('division by zero')}
else{return Math.floor(this/other)}
}else if(isinstance(other,float)){
if(!other.value){throw ZeroDivisionError('division by zero')}
else{return float(Math.floor(this/other.value))}
}else{$UnsupportedOpType("//","int",other.__class__)}
}
Number.prototype.__getattr__=function(attr){throw AttributeError(
"'int' object has no attribute '"+attr+"'")}
Number.prototype.__hash__=function(){return this.valueOf()}
Number.prototype.__in__=function(item){return item.__contains__(this)}
Number.prototype.__int__=function(){return this}
Number.prototype.__mul__=function(other){
var val=this.valueOf()
if(isinstance(other,int)){return this*other}
else if(isinstance(other,float)){return float(this*other.value)}
else if(isinstance(other,bool)){
var bool_value=0
if(other.valueOf())bool_value=1
return this*bool_value}
else if(typeof other==="string"){
var res=''
for(var i=0;i<val;i++){res+=other}
return res
}else if(isinstance(other,[list,tuple])){
var res=[]
var $temp=other.slice(0,other.length)
for(var i=0;i<val;i++){res=res.concat($temp)}
if(isinstance(other,tuple)){res=tuple.apply(this,res)}
return res
}else{$UnsupportedOpType("*",int,other)}
}
Number.prototype.__not_in__=function(item){
res=item.__contains__(this)
return !res
}
Number.prototype.__pow__=function(other){
if(typeof other==="number"){return int(Math.pow(this.valueOf(),other.valueOf()))}
else{$UnsupportedOpType("//",int,other.__class__)}
}
Number.prototype.__setattr__=function(attr,value){throw AttributeError(
"'int' object has no attribute "+attr+"'")}
Number.prototype.__str__=function(){return this.toString()}
Number.prototype.__truediv__=function(other){
if(isinstance(other,int)){
if(other==0){throw ZeroDivisionError('division by zero')}
else{return float(this/other)}
}else if(isinstance(other,float)){
if(!other.value){throw ZeroDivisionError('division by zero')}
else{return float(this/other.value)}
}else{$UnsupportedOpType("//","int",other.__class__)}
}
var $op_func=function(other){
if(isinstance(other,int)){
var res=this.valueOf()-other.valueOf()
if(isinstance(res,int)){return res}
else{return float(res)}
}
else if(isinstance(other,float)){return float(this.valueOf()-other.value)}
else if(isinstance(other,bool)){
var bool_value=0
if(other.valueOf())bool_value=1
return this.valueOf()-bool_value}
else{throw TypeError(
"unsupported operand type(s) for -: "+this.value+" (float) and '"+str(other.__class__)+"'")
}
}
$op_func +='' 
var $ops={'+':'add','-':'sub','%':'mod'}
for($op in $ops){
eval('Number.prototype.__'+$ops[$op]+'__ = '+$op_func.replace(/-/gm,$op))
}
var $comp_func=function(other){
if(isinstance(other,int)){return this.valueOf()> other.valueOf()}
else if(isinstance(other,float)){return this.valueOf()> other.value}
else{throw TypeError(
"unorderable types: "+str(this.__class__)+'() > '+str(other.__class__)+"()")}
}
$comp_func +='' 
var $comps={'>':'gt','>=':'ge','<':'lt','<=':'le','==':'eq','!=':'ne'}
for($op in $comps){
eval("Number.prototype.__"+$comps[$op]+'__ = '+$comp_func.replace(/>/gm,$op))
}
var $notimplemented=function(other){
throw TypeError(
"unsupported operand types for OPERATOR: '"+str(this.__class__)+"' and '"+str(other.__class__)+"'")
}
$notimplemented +='' 
for($op in $operators){
var $opfunc='__'+$operators[$op]+'__'
if(!($opfunc in Number.prototype)){
eval('Number.prototype.'+$opfunc+"="+$notimplemented.replace(/OPERATOR/gm,$op))
}
}
function isinstance(obj,arg){
if(obj===null){return arg===None}
if(obj===undefined){return false}
if(arg.constructor===Array){
for(var i=0;i<arg.length;i++){
if(isinstance(obj,arg[i])){return true}
}
return false
}else{
if(arg===int){
return((typeof obj)=="number"||obj.constructor===Number)&&(obj.valueOf()%1===0)
}
if(arg===float){
return((typeof obj=="number")&&(obj.valueOf()%1!==0))||
(obj.__class__===float)}
if(arg===str){return(typeof obj=="string")}
if(arg===list){return(obj.constructor===Array)}
if(obj.__class__!==undefined){return obj.__class__===arg}
return obj.constructor===arg
}
}
function iter(obj){
if('__item__' in obj){
obj.__counter__=0 
return obj
}
throw TypeError("'"+str(obj.__class__)+"' object is not iterable")
}
function $iterator(obj,info){
this.__getattr__=function(attr){
var res=this[attr]
if(res===undefined){throw AttributeError(
"'"+info+"' object has no attribute '"+attr+"'")}
else{return res}
}
this.__len__=function(){return obj.__len__()}
this.__item__=function(i){return obj.__item__(i)}
this.__class__=new $class(this,info)
this.toString=function(){return info+'('+obj.toString()+')'}
}
function len(obj){
try{return obj.__len__()}
catch(err){throw TypeError("object of type "+obj.__class__+" has no len()")}
}
function map(){
var func=arguments[0],res=[],rank=0
while(true){
var args=[],flag=true
for(var i=1;i<arguments.length;i++){
var x=arguments[i].__item__(rank)
if(x===undefined){flag=false;break}
args.push(x)
}
if(!flag){break}
res.push(func.apply(null,args))
rank++
}
return res
}
function $extreme(args,op){
if(op==='__gt__'){var $op_name="max"}
else{var $op_name="min"}
if(args.length==0){throw TypeError($op_name+" expected 1 argument, got 0")}
var last_arg=args[args.length-1]
var last_i=args.length-1
var has_key=false
if(isinstance(last_arg,$Kw)){
if(last_arg.name==='key'){
var func=last_arg.value
has_key=true
last_i--
}else{throw TypeError($op_name+"() got an unexpected keyword argument")}
}else{var func=function(x){return x}}
if((has_key && args.length==2)||(!has_key && args.length==1)){
var arg=args[0]
var $iter=iter(arg)
var res=null
while(true){
try{
var x=next($iter)
if(res===null || bool(func(x)[op](func(res)))){res=x}
}catch(err){
if(err.name=="StopIteration"){return res}
throw err
}
}
}else{
var res=null
for(var i=0;i<=last_i;i++){
var x=args[i]
if(res===null || bool(func(x)[op](func(res)))){res=x}
}
return res
}
}
function max(){
var args=[]
for(var i=0;i<arguments.length;i++){args.push(arguments[i])}
return $extreme(args,'__gt__')
}
function min(){
var args=[]
for(var i=0;i<arguments.length;i++){args.push(arguments[i])}
return $extreme(args,'__lt__')
}
function next(obj){
if('__item__' in obj){
if(obj.__counter__===undefined){obj.__counter__=0}
var res=obj.__item__(obj.__counter__)
if(res!==undefined){obj.__counter__++;return res}
throw StopIteration()
}
throw TypeError("'"+str(obj.__class__)+"' object is not iterable")
}
function $not(obj){return !bool(obj)}
function $ObjectClass(){
this.__class__="<class 'object'>"
}
$ObjectClass.prototype.__getattr__=function(attr){
if(attr in this){return this[attr]}
else{throw AttributeError("object has no attribute '"+attr+"'")}
}
$ObjectClass.prototype.__delattr__=function(attr){delete this[attr]}
$ObjectClass.prototype.__setattr__=function(attr,value){this[attr]=value}
function object(){
return new $ObjectClass()
}
object.__class__=$type
object.__name__='object'
object.__str__="<class 'object'>"
object.__hash__=function(){
document.$py_next_hash+=1;
return document.$py_next_hash
}
$ObjectClass.prototype.__hash__=object.__hash__
function $open(){
var $ns=$MakeArgs('open',arguments,['file'],{'mode':'r','encoding':'utf-8'},'args','kw')
for(var attr in $ns){eval('var '+attr+'=$ns["'+attr+'"]')}
if(args.length>0){var mode=args[0]}
if(args.length>1){var encoding=args[1]}
if(isinstance(file,JSObject)){return new $OpenFile(file.js,mode,encoding)}
}
function $print(){
var $ns=$MakeArgs('print',arguments,[],{},'args','kw')
var args=$ns['args']
var kw=$ns['kw']
var end='\n'
var res=''
if(kw.__contains__('end')){end=kw.__getitem__('end')}
for(var i=0;i<args.length;i++){
res +=str(args[i])
if(i<args.length-1){res +=' '}
}
res +=end
document.$stdout.__getattr__('write')(res)
}
log=function(arg){console.log(arg)}
function $prompt(text,fill){return prompt(text,fill || '')}
function range(){
var $ns=$MakeArgs('range',arguments,[],{},'args',null)
var args=$ns['args']
if(args.length>3){throw TypeError(
"range expected at most 3 arguments, got "+args.length)
}
var start=0
var stop=0
var step=1
if(args.length==1){stop=args[0]}
else if(args.length>=2){
start=args[0]
stop=args[1]
}
if(args.length>=3){step=args[2]}
if(step==0){throw ValueError("range() arg 3 must not be zero")}
var res=[]
if(step>0){
for(var i=start;i<stop;i+=step){res.push(i)}
}else if(step<0){
for(var i=start;i>stop;i+=step){res.push(i)}
}
return res
}
function repr(obj){return obj.toString()}
function reversed(seq){
if(isinstance(seq,list)){seq.reverse();return seq}
else if(isinstance(seq,str)){
var res=''
for(var i=seq.length-1;i>=0;i--){res+=seq.charAt(i)}
return res
}else{throw TypeError(
"argument to reversed() must be a sequence")}
}
function round(arg,n){
if(!isinstance(arg,[int,float])){
throw TypeError("type "+str(arg.__class__)+" doesn't define __round__ method")
}
if(n===undefined){n=0}
if(!isinstance(n,int)){throw TypeError(
"'"+n.__class__+"' object cannot be interpreted as an integer")}
var mult=Math.pow(10,n)
return Number(Math.round(arg*mult)).__truediv__(mult)
}
function set(){
var i=0
if(arguments.length==0){return new $SetClass()}
else if(arguments.length==1){
var arg=arguments[0]
if(isinstance(arg,set)){return arg}
var obj=new $SetClass()
try{
for(var i=0;i<arg.__len__();i++){
obj.items.push(arg.__getitem__(i))
}
return obj
}catch(err){
throw TypeError("'"+arg.__class__.__name__+"' object is not iterable")
}
}else{
throw TypeError("set expected at most 1 argument, got "+arguments.length)
}
}
set.__class__=$type
set.__name__='set'
set.toString=function(){return "<class 'set'>"}
set.__hash__=function(){throw TypeError("unhashable type: 'set'");}
function $SetClass(){
var x=null
var i=null
this.iter=null
this.__class__=set
this.items=[]
}
$SetClass.prototype.toString=function(){
var res="{"
for(var i=0;i<this.items.length;i++){
var x=this.items[i]
if(isinstance(x,str)){res +="'"+x+"'"}
else{res +=x.toString()}
if(i<this.items.length-1){res +=','}
}
return res+'}'
}
$SetClass.prototype.__add__=function(other){
return set(this.items.concat(other.items))
}
$SetClass.prototype.__class__=set
$SetClass.prototype.__contains__=function(item){
for(var i=0;i<this.items.length;i++){
try{if(this.items[i].__eq__(item)){return True}
}catch(err){void(0)}
}
return False
}
$SetClass.prototype.__eq__=function(other){
if(isinstance(other,set)){
if(other.items.length==this.items.length){
for(var i=0;i<this.items.length;i++){
if(this.__contains__(other.items[i])===False){
return False
}
}
return True
}
}
return False
}
$SetClass.prototype.__hash__=set.__hash__
$SetClass.prototype.__in__=function(item){return item.__contains__(this)}
$SetClass.prototype.__len__=function(){return int(this.items.length)}
$SetClass.prototype.__ne__=function(other){return !(this.__eq__(other))}
$SetClass.prototype.__item__=function(i){return this.items[i]}
$SetClass.prototype.__not_in__=function(item){return !(item.__contains__(this))}
$SetClass.prototype.add=function(item){
var i=0
for(i=0;i<this.items.length;i++){
try{if(item.__eq__(this.items[i])){return}}
catch(err){void(0)}
}
this.items.push(item)
}
function setattr(obj,attr,value){
if(!isinstance(attr,str)){throw TypeError("setattr(): attribute name must be string")}
obj[attr]=value
}
function $SliceClass(start,stop,step){
this.__class__=slice
this.start=start
this.stop=stop
this.step=step
}
function slice(){
var $ns=$MakeArgs('slice',arguments,[],{},'args',null)
var args=$ns['args']
if(args.length>3){throw TypeError(
"slice expected at most 3 arguments, got "+args.length)
}
var start=0
var stop=0
var step=1
if(args.length==1){stop=args[0]}
else if(args.length>=2){
start=args[0]
stop=args[1]
}
if(args.length>=3){step=args[2]}
if(step==0){throw ValueError("slice step must not be zero")}
return new $SliceClass(start,stop,step)
}
function sum(iterable,start){
if(start===undefined){start=0}
var res=0
for(var i=start;i<iterable.__len__();i++){
res=res.__add__(iterable.__item__(i))
}
return res
}
function $tuple(arg){return arg}
function tuple(){
var args=new Array(),i=0
for(i=0;i<arguments.length;i++){args.push(arguments[i])}
var obj=list(args)
obj.__class__=tuple
obj.toString=function(){
var res=args.toString()
res='('+res.substr(1,res.length-2)
if(obj.length===1){res+=','}
return res+')'
}
obj.__hash__=function(){
var x=0x345678
for(var i=0;i < args.length;i++){
var y=args[i].__hash__()
x=(1000003 * x)^ y & 0xFFFFFFFF
}
return x
}
return obj
}
tuple.__class__=$type
tuple.__name__='tuple'
tuple.__str__=function(){return "<class 'tuple'>"}
tuple.toString=tuple.__str__
function zip(){
var $ns=$MakeArgs('zip',arguments,[],{},'args','kw')
var args=$ns['args']
var kw=$ns['kw']
var rank=0,res=[]
while(true){
var line=[],flag=true
for(var i=0;i<args.length;i++){
var x=args[i].__item__(rank)
if(x===undefined){flag=false;break}
line.push(x)
}
if(!flag){return res}
res.push(line)
rank++
}
}
True=true
False=false
Boolean.prototype.__class__=bool
Boolean.prototype.__eq__=function(other){
if(this.valueOf()){return !!other}else{return !other}
}
Boolean.prototype.__hash__=function(){
if(this.valueOf())return 1
return 0
}
Boolean.prototype.__mul__=function(other){
if(this.valueOf())return other
return 0
}
Boolean.prototype.__add__=function(other){
if(this.valueOf())return other + 1
return other
}
Boolean.prototype.toString=function(){
if(this.valueOf())return "True"
return "False"
}
function $NoneClass(){
this.__class__=new $class(this,"NoneType")
this.value=null
this.__bool__=function(){return False}
this.__eq__=function(other){return other===None}
this.__hash__=function(){return 0}
this.__str__=function(){return 'None'}
}
None=new $NoneClass()
Exception=function(msg){
var err=Error()
err.info=''
if(document.$debug && msg.split('\n').length==1){
var module=document.$line_info[1]
var line_num=document.$line_info[0]
var lines=document.$py_src[module].split('\n')
err.info +="\nmodule '"+module+"' line "+line_num
err.info +='\n'+lines[line_num-1]
}
err.message=msg
err.args=tuple(msg.split('\n')[0])
err.__str__=function(){return msg}
err.toString=err.__str__
err.__getattr__=function(attr){return this[attr]}
err.__name__='Exception'
err.__class__=Exception
err.py_error=true
document.$exc_stack.push(err)
return err
}
Exception.__str__=function(){return "<class 'Exception'>"}
Exception.__class__=$type
function $make_exc(name){
var $exc=(Exception+'').replace(/Exception/g,name)
eval(name+'='+$exc)
eval(name+'.__str__ = function(){return "<class '+"'"+name+"'"+'>"}')
eval(name+'.__class__=$type')
}
var $errors=['AssertionError','AttributeError','EOFError','FloatingPointError',
'GeneratorExit','ImportError','IndexError','KeyError','KeyboardInterrupt',
'NameError','NotImplementedError','OSError','OverflowError','ReferenceError',
'RuntimeError','StopIteration','SyntaxError','IndentationError','TabError',
'SystemError','SystemExit','TypeError','UnboundLocalError','ValueError',
'ZeroDivisionError','IOError']
for(var i=0;i<$errors.length;i++){$make_exc($errors[i])}
function $list(){
var args=new Array()
for(var i=0;i<arguments.length;i++){args.push(arguments[i])}
return new $ListClass(args)
}
function list(){
if(arguments.length===0){return[]}
else if(arguments.length>1){
throw TypeError("list() takes at most 1 argument ("+arguments.length+" given)")
}
var res=[]
res.__init__(arguments[0])
return res
}
list.__class__=$type
list.__name__='list'
list.__getattr__=function(attr){
var obj=this
switch(attr){
case 'append':
return $list_append
case 'count':
return $list_count
case 'extend':
return $list_extend
case 'index':
return $list_index
case 'pop':
return $list_pop
case 'remove':
return $list_remove
case 'reverse':
return $list_reverse
case 'sort':
return $list_sort
default:
return this[attr]
}
}
list.__str__=function(){return "<class 'list'>"}
list.toString=list.__str__
function $ListClass(items){
var x=null,i=null
this.iter=null
this.__class__=list
this.items=items 
}
Array.prototype.__add__=function(other){
var res=this.valueOf().concat(other.valueOf())
if(isinstance(this,tuple)){res=tuple.apply(this,res)}
return res
}
Array.prototype.__class__=list
Array.prototype.__contains__=function(item){
for(var i=0;i<this.length;i++){
try{if(this[i].__eq__(item)){return true}
}catch(err){void(0)}
}
return false
}
Array.prototype.__delitem__=function(arg){
if(isinstance(arg,int)){
var pos=arg
if(arg<0){pos=this.length+pos}
if(pos>=0 && pos<this.length){
this.splice(pos,1)
return
}
else{throw IndexError('list index out of range')}
}else if(isinstance(arg,slice)){
var start=arg.start || 0
var stop=arg.stop || this.length
var step=arg.step || 1
if(start<0){start=this.length+start}
if(stop<0){stop=this.length+stop}
var res=[],i=null
if(step>0){
if(stop>start){
for(i=start;i<stop;i+=step){
if(this[i]!==undefined){res.push(i)}
}
}
}else{
if(stop<start){
for(i=start;i>stop;i+=step.value){
if(this[i]!==undefined){res.push(i)}
}
res.reverse()
}
}
for(var i=res.length-1;i>=0;i--){
this.splice(res[i],1)
}
return
}else{
throw TypeError('list indices must be integer, not '+str(arg.__class__))
}
}
Array.prototype.__eq__=function(other){
if(isinstance(other,this.__class__)){
if(other.length==this.length){
for(var i=0;i<this.length;i++){
if(!this[i].__eq__(other[i])){return False}
}
return True
}
}
return False
}
Array.prototype.__getattr__=function(attr){
var obj=this
return function(){
args=[obj]
for(var i=0;i<arguments.length;i++){args.push(arguments[i])}
return list.__getattr__(attr).apply(obj,args)
}
}
Array.prototype.__getitem__=function(arg){
if(isinstance(arg,int)){
var items=this.valueOf()
var pos=arg
if(arg<0){pos=items.length+pos}
if(pos>=0 && pos<items.length){return items[pos]}
else{
throw IndexError('list index out of range')
}
}else if(isinstance(arg,slice)){
var step=arg.step===None ? 1 : arg.step
if(step>0){
var start=arg.start===None ? 0 : arg.start
var stop=arg.stop===None ? this.__len__(): arg.stop
}else{
var start=arg.start===None ? this.__len__()-1 : arg.start
var stop=arg.stop===None ? 0 : arg.stop
}
if(start<0){start=int(this.length+start)}
if(stop<0){stop=this.length+stop}
var res=[],i=null,items=this.valueOf()
if(step>0){
if(stop<=start){return res}
else{
for(i=start;i<stop;i+=step){
if(items[i]!==undefined){res.push(items[i])}
}
return res
}
}else{
if(stop>=start){return res}
else{
for(i=start;i>=stop;i+=step){
if(items[i]!==undefined){res.push(items[i])}
}
return res
}
}
}else if(isinstance(arg,bool)){
return this.__getitem__(int(arg))
}else{
throw TypeError('list indices must be integer, not '+str(arg.__class__))
}
}
Array.prototype.__hash__=function(){
throw TypeError("unhashable type: 'list'")
}
Array.prototype.__init__=function(){
this.splice(0,this.length)
if(arguments.length===0){return}
var arg=arguments[0]
for(var i=0;i<arg.__len__();i++){
this.push(arg.__item__(i))
}
}
Array.prototype.__item__=function(i){return this[i]}
Array.prototype.__in__=function(item){return item.__contains__(this)}
Array.prototype.__len__=function(){return this.length}
Array.prototype.__mul__=function(other){
if(isinstance(other,int)){return other.__mul__(this)}
else{throw TypeError("can't multiply sequence by non-int of type '"+other.__name+"'")}
}
Array.prototype.__ne__=function(other){return !this.__eq__(other)}
Array.prototype.__next__=function(){
if(this.iter===null){this.iter=0}
if(this.iter<this.valueOf().length){
this.iter++
return this.valueOf()[this.iter-1]
}else{
this.iter=null
throw StopIteration()
}
}
Array.prototype.__not_in__=function(item){return !item.__contains__(this)}
Array.prototype.__setitem__=function(arg,value){
if(isinstance(arg,int)){
var pos=arg
if(arg<0){pos=this.length+pos}
if(pos>=0 && pos<this.length){this[pos]=value}
else{throw IndexError('list index out of range')}
}else if(isinstance(arg,slice)){
var start=arg.start===None ? 0 : arg.start
var stop=arg.stop===None ? this.__len__(): arg.stop
var step=arg.step===None ? 1 : arg.step
if(start<0){start=this.length+start}
if(stop<0){stop=this.length+stop}
this.splice(start,stop-start)
if(hasattr(value,'__item__')){
var $temp=list(value)
for(var i=$temp.length-1;i>=0;i--){
this.splice(start,0,$temp[i])
}
}else{
throw TypeError("can only assign an iterable")
}
}else{
throw TypeError('list indices must be integer, not '+str(arg.__class__))
}
}
Array.prototype.toString=function(){
var res="[",i=null,items=this.valueOf()
for(i=0;i<items.length;i++){
var x=items[i]
if(isinstance(x,str)){res +="'"+x+"'"}
else{res +=x.toString()}
if(i<items.length-1){res +=','}
}
return res+']'
}
function $list_append(obj,other){obj.push(other)}
function $list_count(obj,elt){
var res=0
for(var i=0;i<obj.length;i++){
if(obj[i].__eq__(elt)){res++}
}
return res
}
function $list_extend(obj,other){
if(arguments.length!=2){throw TypeError(
"extend() takes exactly one argument ("+arguments.length+" given)")}
try{
for(var i=0;i<other.__len__();i++){
obj.push(other.__item__(i))
}
}catch(err){
throw TypeError("object is not iterable")
}
}
function $list_index(obj,elt){
for(var i=0;i<obj.length;i++){
if(obj[i].__eq__(elt)){return i}
}
throw ValueError(str(elt)+" is not in list")
}
function $list_remove(obj,elt){
for(var i=0;i<obj.length;i++){
if(obj[i].__eq__(elt)){
obj.splice(i,1)
return
}
}
throw ValueError(str(elt)+" is not in list")
}
function $list_pop(obj,elt){
if(arguments.length===1){return obj.pop()}
else if(arguments.length==2){
var pos=arguments[1]
if(isinstance(pos,int)){
var res=obj[pos]
obj.splice(pos,1)
return res
}else{
throw TypeError(pos.__class__+" object cannot be interpreted as an integer")
}
}else{
throw TypeError("pop() takes at most 1 argument ("+arguments.length+' given)')
}
}
function $list_reverse(obj){
for(var i=0;i<parseInt(obj.length/2);i++){
var buf=obj[i]
obj[i]=obj[obj.length-i-1]
obj[obj.length-i-1]=buf
}
}
function $partition(arg,array,begin,end,pivot)
{
var piv=array[pivot]
array.swap(pivot, end-1)
var store=begin
for(var ix=begin;ix<end-1;++ix){
if(arg(array[ix]).__le__(arg(piv))){
array.swap(store, ix)
++store
}
}
array.swap(end-1, store)
return store
}
Array.prototype.swap=function(a, b)
{
var tmp=this[a]
this[a]=this[b]
this[b]=tmp
}
function $qsort(arg,array, begin, end)
{
if(end-1>begin){
var pivot=begin+Math.floor(Math.random()*(end-begin))
pivot=$partition(arg,array, begin, end, pivot)
$qsort(arg,array, begin, pivot)
$qsort(arg,array, pivot+1, end)
}
}
function $list_sort(obj){
var func=function(x){return x}
var reverse=false
for(var i=1;i<arguments.length;i++){
var arg=arguments[i]
if(isinstance(arg,$Kw)){
if(arg.name==='key'){func=arg.value}
else if(arg.name==='reverse'){reverse=arg.value}
}
}
if(obj.length==0){return}
$qsort(func,obj,0,obj.length)
if(reverse){$list_reverse(obj)}
}
function str(arg){
if(arg===undefined){return '<undefined>'}
else if(arg.__str__!==undefined){return arg.__str__()}
else{return arg.toString()}
}
str.__class__=$type
str.__name__='str'
str.__str__=function(){return "<class 'str'>"}
str.toString=str.__str__
String.prototype.__add__=function(other){
if(!(typeof other==="string")){
try{return other.__radd__(this)}
catch(err){throw TypeError(
"Can't convert "+other.__class__+" to str implicitely")}
}else{
return this+other
}
}
String.prototype.__class__=str
String.prototype.__contains__=function(item){
if(!(typeof item==="string")){throw TypeError(
"'in <string>' requires string as left operand, not "+item.__class__)}
var nbcar=item.length
for(var i=0;i<this.length;i++){
if(this.substr(i,nbcar)==item){return True}
}
return False
}
String.prototype.__eq__=function(other){return other===this.valueOf()}
String.prototype.__getattr__=function(attr){
var obj=this
return function(){
args=[obj]
for(var i=0;i<arguments.length;i++){args.push(arguments[i])}
return str.__getattr__(attr).apply(obj,args)
}
}
str.__getattr__=function(attr){
switch(attr){
case 'capitalize':
return $string_capitalize
case 'center': 
return $string_center
case 'count': 
return $string_count
case 'endswith': 
return $string_endswith
case 'find': 
return $string_find
case 'index': 
return $string_index
case 'join':
return $string_join
case 'lower':
return $string_lower
case 'lstrip': 
return $string_lstrip
case 'replace': 
return $string_replace
case 'rfind': 
return $string_rfind
case 'rindex': 
return $string_rindex
case 'rstrip': 
return $string_rstrip
case 'split':
case 'splitfields':
return $string_split
case 'splitlines':
return $string_splitlines
case 'startswith': 
return $string_startswith
case 'strip':
return $string_strip
case 'upper':
return $string_upper
default:
return this[attr]
}
}
String.prototype.__getitem__=function(arg){
if(isinstance(arg,int)){
var pos=arg
if(arg<0){pos=this.length+pos}
if(pos>=0 && pos<this.length){return this.charAt(pos)}
else{throw IndexError('string index out of range')}
}else if(isinstance(arg,slice)){
var step=arg.step===None ? 1 : arg.step
if(step>0){
var start=arg.start===None ? 0 : arg.start
var stop=arg.stop===None ? this.__len__(): arg.stop
}else{
var start=arg.start===None ? this.__len__()-1 : arg.start
var stop=arg.stop===None ? 0 : arg.stop
}
if(start<0){start=this.length+start}
if(stop<0){stop=this.length+stop}
var res='',i=null
if(step>0){
if(stop<=start){return ''}
else{
for(i=start;i<stop;i+=step){
res +=this.charAt(i)
}
}
}else{
if(stop>=start){return ''}
else{
for(i=start;i>=stop;i+=step){
res +=this.charAt(i)
}
}
}
return res
}else if(isinstance(arg,bool)){
return this.__getitem__(int(arg))
}
}
String.prototype.__hash__=function(){
var hash=1
for(var i=0;i < this.length;i++){
hash=(101*hash + this.charCodeAt(i))& 0xFFFFFFFF
}
return hash
}
String.prototype.__in__=function(item){return item.__contains__(this.valueOf())}
String.prototype.__item__=function(i){return this.charAt(i)}
String.prototype.__len__=function(){return this.length}
String.prototype.__mod__=function(args){
var flags=$List2Dict('#','0','-',' ','+')
var ph=[]
function format(s){
var conv_flags='([#\\+\\- 0])*'
var conv_types='[diouxXeEfFgGcrsa%]'
var re=new RegExp('\\%(\\(.+\\))*'+conv_flags+'(\\*|\\d*)(\\.\\*|\\.\\d*)*(h|l|L)*('+conv_types+'){1}')
var res=re.exec(s)
this.is_format=true
if(!res){this.is_format=false;return}
this.src=res[0]
if(res[1]){this.mapping_key=str(res[1].substr(1,res[1].length-2))}
else{this.mapping_key=null}
this.flag=res[2]
this.min_width=res[3]
this.precision=res[4]
this.length_modifier=res[5]
this.type=res[6]
this.toString=function(){
var res='type '+this.type+' key '+this.mapping_key+' min width '+this.min_width
res +=' precision '+this.precision
return res
}
this.format=function(src){
if(this.mapping_key!==null){
if(!isinstance(src,dict)){throw TypeError("format requires a mapping")}
src=src.__getitem__(this.mapping_key)
}
if(this.type=="s"){return str(src)}
else if(this.type=="i" || this.type=="d"){
if(!isinstance(src,[int,float])){throw TypeError(
"%"+this.type+" format : a number is required, not "+str(src.__class__))}
return str(int(src))
}else if(this.type=="f" || this.type=="F"){
if(!isinstance(src,[int,float])){throw TypeError(
"%"+this.type+" format : a number is required, not "+str(src.__class__))}
return str(float(src))
}
}
}
var elts=[]
var pos=0, start=0, nb_repl=0
var val=this.valueOf()
while(pos<val.length){
if(val.charAt(pos)=='%'){
var f=new format(val.substr(pos))
if(f.is_format && f.type!=="%"){
elts.push(val.substring(start,pos))
elts.push(f)
start=pos+f.src.length
pos=start
nb_repl++
}else{pos++}
}else{pos++}
}
elts.push(val.substr(start))
if(!isinstance(args,tuple)){
if(nb_repl>1){throw TypeError('not enough arguments for format string')}
else{elts[1]=elts[1].format(args)}
}else{
if(nb_repl==args.length){
for(var i=0;i<args.length;i++){
var fmt=elts[1+2*i]
elts[1+2*i]=fmt.format(args[i])
}
}else if(nb_repl<args.length){throw TypeError(
"not all arguments converted during string formatting")
}else{throw TypeError('not enough arguments for format string')}
}
var res=''
for(var i=0;i<elts.length;i++){res+=elts[i]}
res=res.replace(/%%/g,'%')
return res
}
String.prototype.__mul__=function(other){
if(!isinstance(other,int)){throw TypeError(
"Can't multiply sequence by non-int of type '"+str(other.__class__)+"'")}
$res=''
for(var i=0;i<other;i++){$res+=this.valueOf()}
return $res
}
String.prototype.__ne__=function(other){return other!==this.valueOf()}
String.prototype.__next__=function(){
if(this.iter==null){this.iter==0}
if(this.iter<this.value.length){
this.iter++
return str(this.value.charAt(this.iter-1))
}else{
this.iter=null
throw StopIteration()
}
}
String.prototype.__not_in__=function(item){return !item.__contains__(this.valueOf())}
String.prototype.__setattr__=function(attr,value){setattr(this,attr,value)}
String.prototype.__setitem__=function(attr,value){
throw TypeError("'str' object does not support item assignment")
}
String.prototype.__str__=function(){
return this.toString()
}
var $comp_func=function(other){
if(typeof other !=="string"){throw TypeError(
"unorderable types: 'str' > "+other.__class__+"()")}
return this > other
}
$comp_func +='' 
var $comps={'>':'gt','>=':'ge','<':'lt','<=':'le'}
for($op in $comps){
eval("String.prototype.__"+$comps[$op]+'__ = '+$comp_func.replace(/>/gm,$op))
}
var $notimplemented=function(other){
throw TypeError(
"unsupported operand types for OPERATOR: '"+str(this.__class__)+"' and '"+str(other.__class__)+"'")
}
$notimplemented +='' 
for($op in $operators){
var $opfunc='__'+$operators[$op]+'__'
if(!($opfunc in String.prototype)){
eval('String.prototype.'+$opfunc+"="+$notimplemented.replace(/OPERATOR/gm,$op))
}
}
function $string_capitalize(obj){
if(obj.length==0){return ''}
return obj.charAt(0).toUpperCase()+obj.substr(1).toLowerCase()
}
function $string_center(obj,width,fillchar){
if(fillchar===undefined){fillchar=' '}else{fillchar=fillchar}
if(width<=obj.length){return obj}
else{
var pad=parseInt((width-obj.length)/2)
res=''
for(var i=0;i<pad;i++){res+=fillchar}
res +=obj
for(var i=0;i<pad;i++){res+=fillchar}
if(res.length<width){res +=fillchar}
return res
}
}
function $string_count(obj,elt){
if(!(typeof elt==="string")){throw TypeError(
"Can't convert '"+str(elt.__class__)+"' object to str implicitly")}
var res=0
for(var i=0;i<obj.length-elt.length+1;i++){
if(obj.substr(i,elt.length)===elt){res++}
}
return res
}
function $string_endswith(obj){
var args=[]
for(var i=1;i<arguments.length;i++){args.push(arguments[i])}
var $ns=$MakeArgs("str.endswith",args,['suffix'],
{'start':null,'end':null},null,null)
var suffixes=$ns['suffix']
if(!isinstance(suffixes,tuple)){suffixes=[suffixes]}
var start=$ns['start']|| 0
var end=$ns['end']|| obj.length-1
var s=obj.substr(start,end+1)
for(var i=0;i<suffixes.length;i++){
suffix=suffixes[i]
if(suffix.length<=s.length &&
s.substr(s.length-suffix.length)==suffix){return True}
}
return False
}
function $string_find(obj){
var args=[]
for(var i=1;i<arguments.length;i++){args.push(arguments[i])}
var $ns=$MakeArgs("str.find",args,['sub'],
{'start':0,'end':obj.length},null,null)
var sub=$ns['sub'],start=$ns['start'],end=$ns['end']
if(!isinstance(sub,str)){throw TypeError(
"Can't convert '"+str(sub.__class__)+"' object to str implicitly")}
if(!isinstance(start,int)||!isinstance(end,int)){throw TypeError(
"slice indices must be integers or None or have an __index__ method")}
var s=obj.substring(start,end)
var escaped=list("[.*+?|()$^")
var esc_sub=''
for(var i=0;i<sub.length;i++){
if(escaped.indexOf(sub.charAt(i))>-1){esc_sub +='\\'}
esc_sub +=sub.charAt(i)
}
var res=s.search(esc_sub)
if(res==-1){return -1}
else{return start+res}
}
function $string_index(obj){
var args=[]
for(var i=0;i<arguments.length;i++){args.push(arguments[i])}
var res=$string_find.apply(obj,args)
if(res===-1){throw ValueError("substring not found")}
else{return res}
}
function $string_join(obj,iterable){
if(!'__item__' in iterable){throw TypeError(
"'"+str(iterable.__class__)+"' object is not iterable")}
var res='',count=0
for(var i=0;i<iterable.length;i++){
var obj2=iterable.__getitem__(i)
if(!isinstance(obj2,str)){throw TypeError(
"sequence item "+count+": expected str instance, "+obj2.__class__+"found")}
res +=obj2+obj
count++
}
if(count==0){return ''}
res=res.substr(0,res.length-obj.length)
return res
}
function $string_lower(obj){return obj.toLowerCase()}
function $string_lstrip(obj,x){
var pattern=null
if(x==undefined){pattern="\\s*"}
else{pattern="["+x+"]*"}
var sp=new RegExp("^"+pattern)
return obj.replace(sp,"")
}
function $re_escape(str)
{
var specials="[.*+?|()$^"
for(var i=0;i<specials.length;i++){
var re=new RegExp('\\'+specials.charAt(i),'g')
str=str.replace(re, "\\"+specials.charAt(i))
}
return str
}
function $string_replace(obj,old,_new,count){
if(count!==undefined){
if(!isinstance(count,[int,float])){throw TypeError(
"'"+str(count.__class__)+"' object cannot be interpreted as an integer")}
var re=new RegExp($re_escape(old),'g')
var res=obj.valueOf()
while(count>0){
if(obj.search(re)==-1){return res}
res=res.replace(re,_new)
count--
}
return res
}else{
var re=new RegExp($re_escape(old),"g")
return obj.replace(re,_new)
}
}
function $string_rfind(obj){
var args=[]
for(var i=1;i<arguments.length;i++){args.push(arguments[i])}
var $ns=$MakeArgs("str.find",args,['sub'],
{'start':0,'end':obj.length},null,null)
var sub=$ns['sub'],start=$ns['start'],end=$ns['end']
if(!isinstance(sub,str)){throw TypeError(
"Can't convert '"+str(sub.__class__)+"' object to str implicitly")}
if(!isinstance(start,int)||!isinstance(end,int)){throw TypeError(
"slice indices must be integers or None or have an __index__ method")}
var s=obj.substring(start,end)
var reversed=''
for(var i=s.length-1;i>=0;i--){reversed +=s.charAt(i)}
var res=reversed.search(sub)
if(res==-1){return -1}
else{return start+s.length-1-res}
}
function $string_rindex(obj){
var args=[]
for(var i=0;i<arguments.length;i++){args.push(arguments[i])}
var res=$string_rfind.apply(obj,arguments)
if(res==-1){throw ValueError("substring not found")}
else{return res}
}
function $string_rstrip(obj,x){
if(x==undefined){pattern="\\s*"}
else{pattern="["+x+"]*"}
sp=new RegExp(pattern+'$')
return str(obj.replace(sp,""))
}
function $string_split(obj){
var args=[]
for(var i=1;i<arguments.length;i++){args.push(arguments[i])}
var $ns=$MakeArgs("str.split",args,[],{},'args','kw')
var sep=null,maxsplit=-1
if($ns['args'].length>=1){sep=$ns['args'][0]}
if($ns['args'].length==2){maxsplit=$ns['args'][1]}
if(sep===null){var re=/\s/}
else{
var escaped=list('*.[]()|$^')
var esc_sep=''
for(var i=0;i<sep.length;i++){
if(escaped.indexOf(sep.charAt(i))>-1){esc_sep +='\\'}
esc_sep +=sep.charAt(i)
}
var re=new RegExp(esc_sep)
}
if(maxsplit==-1)return obj.split(re,maxsplit)
var l=obj.split(re,-1)
var a=l.splice(0, maxsplit)
var b=l.splice(maxsplit-1, l.length)
a.push(b.join(sep))
return a
}
function $string_splitlines(obj){return $string_split(obj,'\n')}
function $string_startswith(obj){
var args=[]
for(var i=1;i<arguments.length;i++){args.push(arguments[i])}
$ns=$MakeArgs("str.startswith",args,['prefix'],
{'start':null,'end':null},null,null)
var prefixes=$ns['prefix']
if(!isinstance(prefixes,tuple)){prefixes=[prefixes]}
var start=$ns['start']|| 0
var end=$ns['end']|| obj.length-1
var s=obj.substr(start,end+1)
for(var i=0;i<prefixes.length;i++){
prefix=prefixes[i]
if(prefix.length<=s.length &&
s.substr(0,prefix.length)==prefix){return True}
}
return False
}
function $string_strip(obj,x){
if(x==undefined){x="\\s"}
pattern="["+x+"]"
return $string_rstrip($string_lstrip(obj,x),x)
}
function $string_upper(obj){return obj.toUpperCase()}
function $importer(){
if(window.XMLHttpRequest){
var $xmlhttp=new XMLHttpRequest()
}else{
var $xmlhttp=new ActiveXObject("Microsoft.XMLHTTP")
}
var fake_qs='?foo='+Math.random().toString(36).substr(2,8)
var timer=setTimeout(function(){
$xmlhttp.abort()
throw ImportError("No module named '"+module+"'")}, 5000)
return[$xmlhttp,fake_qs,timer]
}
function $import_js(module,alias,names){
var imp=$importer()
var $xmlhttp=imp[0],fake_qs=imp[1],timer=imp[2],res=null
$xmlhttp.onreadystatechange=function(){
if($xmlhttp.readyState==4){
window.clearTimeout(timer)
if($xmlhttp.status==200 || $xmlhttp.status==0){res=$xmlhttp.responseText}
else{
res=Error()
res.name='NotFoundError'
res.message="No module named '"+module+"'"
}
}
}
$xmlhttp.open('GET',__BRYTHON__.brython_path+'libs/'+module+'.js'+fake_qs,false)
if('overrideMimeType' in $xmlhttp){$xmlhttp.overrideMimeType("text/plain")}
$xmlhttp.send()
if(res.constructor===Error){throw res}
try{
eval(res)
if(eval('$module')===undefined){
throw ImportError("name '$module' is not defined in module")
}
if(alias===undefined){alias=module}
if(names===undefined){
eval(alias+'=$module')
eval(alias+'.__class__ = $type')
eval(alias+'.__str__ = function(){return "<module \''+module+"'>\"}")
eval(alias+'.__file__ = "' +document.$brython_path+'libs/'+ module + '.js"')
}else{
if(names.length===1 && names[0]==='*'){
for(var name in $module){
if(name.substr(0,1)==='_'){continue}
eval(name+'=$module[name]')
}
}else{
for(var i=0;i<names.length;i++){
eval(names[i]+'=$module[names[i]]')
}
}
}
}catch(err){throw ImportError(err.message)}
}
function $import_py(module,alias,names){
var flag=false
for(var i=0;i<__BRYTHON__.path.length;i++){
relpath=__BRYTHON__.path[i]
try{
$import_py1(module,alias,names,relpath)
flag=true
}catch(err){
void(0)
}
if(flag){break}
relpath=__BRYTHON__.path[i]+'/'+module
try{
$import_py1('__init__',alias,names,relpath)
flag=true
}catch(err){console.log(err)
void(0)
}
if(flag){break}
}
if(!flag){throw ImportError("No module named '"+module+"'")}
}
function $import_py1(module,alias,names,relpath){
var imp=$importer()
var $xmlhttp=imp[0],fake_qs=imp[1],timer=imp[2],res=null
var module_path
$xmlhttp.onreadystatechange=function(){
if($xmlhttp.readyState==4){
window.clearTimeout(timer)
if($xmlhttp.status==200 || $xmlhttp.status==0){res=$xmlhttp.responseText}
else{
res=Error('ImportError',"No module named '"+module+"'")
}
}
}
module_path=relpath+"/"+ module + ".py"
$xmlhttp.open('GET',module_path+fake_qs,false)
$xmlhttp.send()
if(relpath===undefined && res.constructor===Error){
module_path=document.$brython_path+"tests/"+module + "/__init__.py"
res=null
$xmlhttp.open('GET',module+'/__init__.py'+fake_qs,false)
$xmlhttp.send()
}
if(res.constructor===Error){res.name='ImportError';throw res}
document.$py_module_path[module]=module_path
var root=__BRYTHON__.py2js(res,module)
var body=root.children
root.children=[]
var mod_node=new $Node('expression')
if(names!==undefined){alias='$module'}
new $NodeJSCtx(mod_node,alias+'=(function()')
root.insert(0,mod_node)
mod_node.children=body
var mod_names=[]
for(var i=1;i<mod_node.children.length;i++){
var node=mod_node.children[i]
var ctx=node.get_ctx().tree[0]
if(ctx.type==='def'||ctx.type==='class'){
if(mod_names.indexOf(ctx.name)===-1){mod_names.push(ctx.name)}
}else if(ctx.type==='assign'){
var left=ctx.tree[0]
if(left.type==='expr'&&left.tree[0].type==='id'&&left.tree[0].tree.length===0){
var id_name=left.tree[0].value
if(mod_names.indexOf(id_name)===-1){mod_names.push(id_name)}
}
}
}
var ret_code='return {'
for(var i=0;i<mod_names.length;i++){
ret_code +=mod_names[i]+':'+mod_names[i]+','
}
ret_code +='__getattr__:function(attr){return this[attr]},'
ret_code +='__setattr__:function(attr,value){this[attr]=value}'
ret_code +='}'
var ret_node=new $Node('expression')
new $NodeJSCtx(ret_node,ret_code)
mod_node.add(ret_node)
var ex_node=new $Node('expression')
new $NodeJSCtx(ex_node,')()')
root.add(ex_node)
if(names!==undefined){
if(names.length===1 && names[0]==='*'){
var new_node=new $Node('expression')
new $NodeJSCtx(new_node,'for(var $attr in $module)')
root.add(new_node)
var attr_node=new $Node('expression')
new $NodeJSCtx(attr_node,'if($attr.charAt(0)!=="_"){eval($attr+"=$module[$attr]")}')
new_node.add(attr_node)
}else{
for(var i=0;i<names.length;i++){
var new_node=new $Node('expression')
new $NodeJSCtx(new_node,names[i]+'=$module.'+names[i])
root.add(new_node)
}
}
}
try{
var js=root.to_js()
eval(js)
eval(alias+'.__class__ = $type')
eval(alias+'.__str__ = function(){return "<module \''+module+"'>\"}")
eval(alias+'.__file__ = "' + module_path + '"')
}catch(err){
eval('throw '+err.name+'(err.message)')
}
}
$import_funcs=[$import_js,$import_py]
function $import_single(name,alias,names){
for(var j=0;j<$import_funcs.length;j++){
try{$import_funcs[j](name,alias,names);return}
catch(err){
if(err.name==="NotFoundError"){
if(j==$import_funcs.length-1){
throw ImportError("no module named '"+name+"'")
}else{
continue
}
}else{throw(err)}
}
}
}
function $import_list(modules){
for(var i=0;i<modules.length;i++){
var module=modules[i][0]
$import_single(modules[i][0],modules[i][1])
document.$py_module_alias[modules[i][0]]=modules[i][1]
}
}
function $import_from(module,names,parent_module){
var relpath
var alias=module
if(parent_module !=="undefined"){
throw ImportError('from .. import .. not supported yet')
relpath=document.$py_module_path[parent_module]
var i=relpath.lastIndexOf('/')
relpath=relpath.substring(0, i)
alias=document.$py_module_alias[parent_module]
}else{
$import_single(module,module,names)
}
}
var $operators={
"//=":"ifloordiv",">>=":"irshift","<<=":"ilshift",
"**=":"ipow","**":"pow","//":"floordiv","<<":"lshift",">>":"rshift",
"+=":"iadd","-=":"isub","*=":"imul","/=":"itruediv",
"%=":"imod","&=":"iand","|=":"ior",
"^=":"ipow","+":"add","-":"sub","*":"mul",
"/":"truediv","%":"mod","&":"and","|":"or",
"^":"pow","<":"lt",">":"gt",
"<=":"le",">=":"ge","==":"eq","!=":"ne",
"or":"or","and":"and", "in":"in", 
"is":"is","not_in":"not_in","is_not":"is_not" 
}
var $op_weight={
'or':1,'and':2,
'in':3,'not_in':3,
'<':4, '<=':4, '>':4, '>=':4, '!=':4, '==':4,'is':4,
'+':5,
'-':6,
'/':7,'//':7,'%':7,
'*':8,
'**':9
}
var $augmented_assigns={
"//=":"ifloordiv",">>=":"irshift","<<=":"ilshift",
"**=":"ipow","+=":"iadd","-=":"isub","*=":"imul","/=":"itruediv",
"%=":"imod","^=":"ipow"
}
function $_SyntaxError(C,msg){
var ctx_node=C
while(ctx_node.type!=='node'){ctx_node=ctx_node.parent}
var tree_node=ctx_node.node
var module=tree_node.module
var line_num=tree_node.line_num
document.$line_info=[line_num,module]
$SyntaxError(module,msg,$pos)
}
var $first_op_letter={}
for(op in $operators){$first_op_letter[op.charAt(0)]=0}
function $Node(type){
this.type=type
this.children=[]
this.add=function(child){
this.children.push(child)
child.parent=this
}
this.insert=function(pos,child){
this.children.splice(pos,0,child)
child.parent=this
}
this.toString=function(){return "<object 'Node'>"}
this.show=function(indent){
var res=''
if(this.type==='module'){
for(var i=0;i<this.children.length;i++){
res +=this.children[i].show(indent)
}
}else{
indent=indent || 0
for(var i=0;i<indent;i++){res+=' '}
res +=this.C
if(this.children.length>0){res +='{'}
res +='\n'
for(var i=0;i<this.children.length;i++){
res +='['+i+'] '+this.children[i].show(indent+4)
}
if(this.children.length>0){
for(var i=0;i<indent;i++){res+=' '}
res+='}\n'
}
}
return res
}
this.to_js=function(indent){
var res=''
if(this.type==='module'){
for(var i=0;i<this.children.length;i++){
res +=this.children[i].to_js(indent)
}
}else{
indent=indent || 0
var ctx_js=this.C.to_js(indent)
if(ctx_js){
for(var i=0;i<indent;i++){res+=' '}
res +=ctx_js
if(this.children.length>0){res +='{'}
res +='\n'
for(var i=0;i<this.children.length;i++){
res +=this.children[i].to_js(indent+4)
}
if(this.children.length>0){
for(var i=0;i<indent;i++){res+=' '}
res+='}\n'
}
}
}
return res
}
this.transform=function(rank){
var res=''
if(this.type==='module'){
var i=0
while(i<this.children.length){
var node=this.children[i]
this.children[i].transform(i)
i++
}
}else{
var elt=this.C.tree[0]
if(elt.transform !==undefined){
elt.transform(this,rank)
}
var i=0
while(i<this.children.length){
this.children[i].transform(i)
i++
}
}
}
this.get_ctx=function(){return this.C}
}
function $last(src){return src[src.length-1]}
var $loop_id=0
function $AbstractExprCtx(C,with_commas){
this.type='abstract_expr'
this.with_commas=with_commas
this.name=name
this.parent=C
this.tree=[]
C.tree.push(this)
this.toString=function(){return '(abstract_expr '+with_commas+') '+this.tree}
this.to_js=function(){
if(this.type==='list'){return '['+$to_js(this.tree)+']'}
else{return $to_js(this.tree)}
}
}
function $AssertCtx(C){
this.type='assert'
this.toString=function(){return '(assert) '+this.tree}
this.parent=C
this.tree=[]
C.tree.push(this)
this.transform=function(node,rank){
var new_ctx=new $ConditionCtx(node.C,'if')
var not_ctx=new $NotCtx(new_ctx)
not_ctx.tree=[this.tree[0]]
node.C=new_ctx
var new_node=new $Node('expression')
var js='throw AssertionError("")'
if(this.tree.length==2){
js='throw AssertionError(str('+this.tree[1].to_js()+'))'
}
new $NodeJSCtx(new_node,js)
node.add(new_node)
}
}
function $AssignCtx(C){
this.type='assign'
C.parent.tree.pop()
C.parent.tree.push(this)
this.parent=C.parent
this.tree=[C]
this.toString=function(){return '(assign) '+this.tree[0]+'='+this.tree[1]}
this.transform=function(node,rank){
var left=this.tree[0]
while(left.type==='assign'){
var new_node=new $Node('expression')
var node_ctx=new $NodeCtx(new_node)
node_ctx.tree=[left]
node.parent.insert(rank+1,new_node)
this.tree[0]=left.tree[1]
left=this.tree[0]
}
var left_items=null
if(left.type==='expr' && left.tree.length>1){
var left_items=left.tree
}else if(left.type==='expr' && left.tree[0].type==='list_or_tuple'){
var left_items=left.tree[0].tree
}else if(left.type==='target_list'){
var left_items=left.tree
}else if(left.type==='list_or_tuple'){
var left_items=left.tree
}
if(left_items===null){return}
var right=this.tree[1]
var right_items=null
if(right.type==='list'||right.type==='tuple'||
(right.type==='expr' && right.tree.length>1)){
var right_items=right.tree
}
if(right_items!==null){
if(right_items.length>left_items.length){
throw Error('ValueError : too many values to unpack (expected '+left_items.length+')')
}else if(right_items.length<left_items.length){
throw Error('ValueError : need more than '+right_items.length+' to unpack')
}
var new_nodes=[]
var new_node=new $Node('expression')
new $NodeJSCtx(new_node,'void(0)')
new_nodes.push(new_node)
var new_node=new $Node('expression')
new $NodeJSCtx(new_node,'var $temp'+$loop_num+'=[]')
new_nodes.push(new_node)
for(var i=0;i<right_items.length;i++){
var js='$temp'+$loop_num+'.push('+right_items[i].to_js()+')'
var new_node=new $Node('expression')
new $NodeJSCtx(new_node,js)
new_nodes.push(new_node)
}
for(var i=0;i<left_items.length;i++){
var new_node=new $Node('expression')
var C=new $NodeCtx(new_node)
left_items[i].parent=C
var assign=new $AssignCtx(left_items[i])
assign.tree[1]=new $JSCode('$temp'+$loop_num+'['+i+']')
new_nodes.push(new_node)
}
node.parent.children.splice(rank,1)
for(var i=new_nodes.length-1;i>=0;i--){
node.parent.insert(rank,new_nodes[i])
}
$loop_num++
}else{
var new_node=new $Node('expression')
new $NodeJSCtx(new_node,'$right='+right.to_js())
var new_nodes=[new_node]
for(var i=0;i<left_items.length;i++){
var new_node=new $Node('expression')
var C=new $NodeCtx(new_node)
left_items[i].parent=C
var assign=new $AssignCtx(left_items[i])
assign.tree[1]=new $JSCode('$right.__item__('+i+')')
new_nodes.push(new_node)
}
node.parent.children.splice(rank,1)
for(var i=new_nodes.length-1;i>=0;i--){
node.parent.insert(rank,new_nodes[i])
}
}
}
this.to_js=function(){
if(this.parent.type==='call'){
return '$Kw('+this.tree[0].to_js()+','+this.tree[1].to_js()+')'
}else{
var left=this.tree[0]
if(left.type==='expr'){
left=left.tree[0]
}
var right=this.tree[1]
if(left.type==='attribute'){
left.func='setattr'
var res=left.to_js()
left.func='getattr'
res=res.substr(0,res.length-1)
res +=','+right.to_js()+')'
return res
}else if(left.type==='sub'){
left.func='setitem' 
var res=left.to_js()
res=res.substr(0,res.length-1)
left.func='getitem' 
res +=','+right.to_js()+')'
return res
}
var scope=$get_scope(this)
if(scope===null){
return left.to_js()+'='+right.to_js()
}else if(scope.ntype==='def'){
if(scope.globals && scope.globals.indexOf(left.value)>-1){
return left.to_js()+'='+right.to_js()
}else{
return 'var '+left.to_js()+'='+right.to_js()
}
}else if(scope.ntype==='class'){
var attr=left.to_js()
return 'var '+attr+' = $class.'+attr+'='+right.to_js()
}
}
}
}
function $AttrCtx(C){
this.type='attribute'
this.value=C.tree[0]
this.parent=C
C.tree.pop()
C.tree.push(this)
this.tree=[]
this.func='getattr' 
this.toString=function(){return '(attr) '+this.value+'.'+this.name}
this.to_js=function(){
var name=this.name
if(name.substr(0,2)==='$$'){name=name.substr(2)}
if(name.substr(0,2)!=='__'){name='__'+this.func+'__("'+name+'")'}
return this.value.to_js()+'.'+name
}
}
function $CallArgCtx(C){
this.type='call_arg'
this.toString=function(){return 'call_arg '+this.tree}
this.parent=C
this.tree=[]
C.tree.push(this)
this.expect='id'
this.to_js=function(){return $to_js(this.tree)}
}
function $CallCtx(C){
this.type='call'
this.func=C.tree[0]
this.parent=C
C.tree.pop()
C.tree.push(this)
this.tree=[]
this.toString=function(){return '(call) '+this.func+'('+this.tree+')'}
this.to_js=function(){return this.func.to_js()+'('+$to_js(this.tree)+')'}
}
function $ClassCtx(C){
this.type='class'
this.parent=C
this.tree=[]
C.tree.push(this)
this.expect='id'
this.toString=function(){return 'class '+this.tree}
this.transform=function(node,rank){
var instance_decl=new $Node('expression')
new $NodeJSCtx(instance_decl,'var $class = new Object()')
node.insert(0,instance_decl)
var ret_obj=new $Node('expression')
new $NodeJSCtx(ret_obj,'return $class')
node.insert(node.children.length,ret_obj)
var run_func=new $Node('expression')
new $NodeJSCtx(run_func,')()')
node.parent.insert(rank+1,run_func)
var scope=$get_scope(this)
if(scope===null||scope.ntype!=='class'){
js='var '+this.name
}else{
js='var '+this.name+' = $class.'+this.name
}
js +='=$class_constructor("'+this.name+'",$'+this.name
if(this.tree.length>0 && this.tree[0].tree.length>0){
js +=','+$to_js(this.tree[0].tree)
}
js +=')'
var cl_cons=new $Node('expression')
new $NodeJSCtx(cl_cons,js)
node.parent.insert(rank+2,cl_cons)
if(scope===null && this.parent.node.module==='__main__'){
js='window.'+this.name+'='+this.name
var w_decl=new $Node('expression')
new $NodeJSCtx(w_decl,js)
node.parent.insert(rank+3,w_decl)
}
}
this.to_js=function(){
return 'var $'+this.name+'=(function()'
}
}
function $CompIfCtx(C){
this.type='comp_if'
C.parent.intervals.push($pos)
this.parent=C
this.tree=[]
C.tree.push(this)
this.toString=function(){return '(comp if) '+this.tree}
this.to_js=function(){return 'comp if to js'}
}
function $ComprehensionCtx(C){
this.type='comprehension'
this.parent=C
this.tree=[]
C.tree.push(this)
this.toString=function(){return '(comprehension) '+this.tree}
this.to_js=function(){
var intervals=[]
for(var i=0;i<this.tree.length;i++){
intervals.push(this.tree[i].start)
}
return intervals
}
}
function $CompForCtx(C){
this.type='comp_for'
C.parent.intervals.push($pos)
this.parent=C
this.tree=[]
this.expect='in'
C.tree.push(this)
this.toString=function(){return '(comp for) '+this.tree}
this.to_js=function(){return 'comp for to js'}
}
function $CompIterableCtx(C){
this.type='comp_iterable'
this.parent=C
this.tree=[]
C.tree.push(this)
this.toString=function(){return '(comp iter) '+this.tree}
this.to_js=function(){return 'comp iter to js'}
}
function $ConditionCtx(C,token){
this.type='condition'
this.token=token
this.parent=C
this.tree=[]
C.tree.push(this)
this.toString=function(){return this.token+' '+this.tree}
this.to_js=function(){
var tok=this.token
if(tok==='elif'){tok='else if'}
if(this.tree.length==1){
var res=tok+'(bool('+$to_js(this.tree)+'))'
}else{
var res=tok+'(bool('+this.tree[0].to_js()+'))'
if(this.tree[1].tree.length>0){
res +='{'+this.tree[1].to_js()+'}'
}
}
return res
}
}
function $DecoratorCtx(C){
this.type='decorator'
this.parent=C
C.tree.push(this)
this.tree=[]
this.toString=function(){return '(decorator) '+this.tree}
this.to_js=function(){return $to_js(this.tree)}
}
function $DefCtx(C){
this.type='def'
this.name=null
this.parent=C
this.tree=[]
C.tree.push(this)
this.toString=function(){return 'def '+this.name+'('+this.tree+')'}
this.transform=function(node,rank){
if(this.transformed!==undefined){return}
this.rank=rank 
if(this.in_line!==undefined){
var new_node=new $Node('expression')
var ctx=new $NodeCtx(new_node)
ctx.tree=[this.tree[this.tree.length-1]]
node.add(new_node)
}
var scope=$get_scope(this)
var required=''
var defaults=''
var other_args=null
var other_kw=null
var env=[]
for(var i=0;i<this.tree[0].tree.length;i++){
var arg=this.tree[0].tree[i]
if(arg.type==='func_arg_id'){
if(arg.tree.length===0){required+='"'+arg.name+'",'}
else{
defaults+='"'+arg.name+'":'+$to_js(arg.tree)+','
if(arg.tree[0].type==='expr' 
&& arg.tree[0].tree[0].type==='id'){
env.push(arg.tree[0].tree[0].value)
}
}
}else if(arg.type==='func_star_arg'&&arg.op==='*'){other_args='"'+arg.name+'"'}
else if(arg.type==='func_star_arg'&&arg.op==='**'){other_kw='"'+arg.name+'"'}
}
this.env=env
if(required.length>0){required=required.substr(0,required.length-1)}
if(defaults.length>0){defaults=defaults.substr(0,defaults.length-1)}
var js='var $ns=$MakeArgs("'+this.name+'",arguments,['+required+'],'
js +='{'+defaults+'},'+other_args+','+other_kw+')'
var new_node1=new $Node('expression')
new $NodeJSCtx(new_node1,js)
var js='for($var in $ns){eval("var "+$var+"=$ns[$var]")}'
var new_node2=new $Node('expression')
new $NodeJSCtx(new_node2,js)
node.children.splice(0,0,new_node1,new_node2)
var try_node=new $Node('expression')
new $NodeJSCtx(try_node,'try')
var def_func_node=new $Node('expression')
new $NodeJSCtx(def_func_node,'return function()')
try_node.add(def_func_node)
for(var i=0;i<node.children.length;i++){
def_func_node.add(node.children[i])
}
var ret_node=new $Node('expression')
var catch_node=new $Node('expression')
var js='catch(err'+$loop_num+')'
js +='{$raise(err'+$loop_num+'.name,err'+$loop_num+'.message)}'
new $NodeJSCtx(catch_node,js)
node.children=[]
node.add(try_node)
node.add(catch_node)
var txt=')('
for(var i=0;i<this.env.length;i++){
txt +=this.env[i]
if(i<this.env.length-1){txt +=','}
}
new $NodeJSCtx(ret_node,txt+')')
node.parent.insert(rank+1,ret_node)
js=this.name+'.__name__'
if(scope !==null && scope.ntype==='class'){
js +='=$class.'+this.name+'.__name__'
}
js +='="'+this.name+'"'
var name_decl=new $Node('expression')
new $NodeJSCtx(name_decl,js)
node.parent.children.splice(rank+2,0,name_decl)
if(scope===null && node.module==='__main__'){
js='window.'+this.name+'='+this.name
new_node1=new $Node('expression')
new $NodeJSCtx(new_node1,js)
node.parent.children.splice(rank+3,0,new_node1)
}
this.transformed=true
}
this.add_generator_declaration=function(){
var scope=$get_scope(this)
var node=this.parent.node
if(this.type==='generator'){
js=this.name
if(scope.ntype==='class'){js +="=$class."+this.name}
js +='=$generator($'+this.name+')'
var gen_node=new $Node('expression')
new $NodeJSCtx(gen_node,js)
node.parent.children.splice(this.rank+2,0,gen_node)
}
}
this.to_js=function(){
var scope=$get_scope(this)
var name=this.name
if(this.type==='generator'){name='$'+name}
if(scope===null || scope.ntype!=='class'){
res=name+'= (function ('
}else{
res='var '+name+' = $class.'+name+'= (function ('
}
for(var i=0;i<this.env.length;i++){
res+=this.env[i]
if(i<this.env.length-1){res+=','}
}
res +=')'
return res
}
}
function $DelCtx(C){
this.type='del'
this.parent=C
C.tree.push(this)
this.tree=[]
this.toString=function(){return 'del '+this.tree}
this.to_js=function(){
res=[]
var tree=this.tree[0].tree
for(var i=0;i<tree.length;i++){
var expr=tree[i]
if(expr.type==='expr'||expr.type==='id'){
res.push('delete '+expr.to_js())
}else if(expr.type==='sub'){
expr.func='delitem'
res.push(expr.to_js())
expr.func='getitem'
}else{
throw SyntaxError("wrong argument for del "+expr.type)
}
}
return res.join(';')
}
}
function $DictCtx(C){
this.type='dict'
this.parent=C.parent
C.parent.tree.pop()
C.parent.tree.push(this)
C.name='dict_key'
this.tree=[C]
this.expect=','
this.toString=function(){return 'dict '+this.tree}
}
function $DictOrSetCtx(C){
this.type='dict_or_set'
this.real='dict_or_set'
this.expect='id'
this.closed=false
this.toString=function(){
if(this.real==='dict'){return '(dict) {'+this.tree+'}'}
else if(this.real==='set'){return '(set) {'+this.tree+'}'}
else{return '(dict_or_set) {'+this.tree+'}'}
}
this.parent=C
this.tree=[]
C.tree.push(this)
this.to_js=function(){
if(this.real==='dict'){
var res='dict(['
for(var i=0;i<this.items.length;i+=2){
res+='['+this.items[i].to_js()+','+this.items[i+1].to_js()+']'
if(i<this.items.length-2){res+=','}
}
return res+'])'+$to_js(this.tree)
}else{return 'set(['+$to_js(this.items)+'])'+$to_js(this.tree)}
}
}
function $DoubleStarArgCtx(C){
this.type='double_star_arg'
this.parent=C
this.tree=[]
C.tree.push(this)
this.toString=function(){return '**'+this.tree}
this.to_js=function(){return '$pdict('+$to_js(this.tree)+')'}
}
function $ExceptCtx(C){
this.type='except'
this.parent=C
C.tree.push(this)
this.tree=[]
this.expect='id'
this.toString=function(){return '(except) '}
this.to_js=function(){
if(this.tree.length===0){return 'else'}
else{
var res='else if(['
for(var i=0;i<this.tree.length;i++){
res+='"'+this.tree[i].name+'"'
if(i<this.tree.length-1){res+=','}
}
res +='].indexOf('+this.error_name+'.__name__)>-1)'
return res
}
}
}
function $ExprCtx(C,name,with_commas){
this.type='expr'
this.name=name
this.with_commas=with_commas
this.expect=',' 
this.parent=C
this.tree=[]
C.tree.push(this)
this.toString=function(){return '(expr '+with_commas+') '+this.tree}
this.to_js=function(){
if(this.type==='list'){return '['+$to_js(this.tree)+']'}
else if(this.tree.length===1){return this.tree[0].to_js()}
else{return 'tuple('+$to_js(this.tree)+')'}
}
}
function $ExprNot(C){
this.type='expr_not'
this.toString=function(){return '(expr_not)'}
this.parent=C
this.tree=[]
C.tree.push(this)
}
function $FloatCtx(C,value){
this.type='float'
this.value=value
this.toString=function(){return 'float '+this.value}
this.parent=C
this.tree=[]
C.tree.push(this)
this.to_js=function(){return 'float('+this.value+')'}
}
function $ForTarget(C){
this.type='for_target'
this.parent=C
this.tree=[]
C.tree.push(this)
this.toString=function(){return 'for_target'+' '+this.tree}
this.to_js=function(){return $to_js(this.tree)}
}
function $ForExpr(C){
this.type='for'
this.parent=C
this.tree=[]
C.tree.push(this)
this.toString=function(){return '(for) '+this.tree}
this.transform=function(node,rank){
var new_nodes=[]
var new_node=new $Node('expression')
var target=this.tree[0]
var iterable=this.tree[1]
new $NodeJSCtx(new_node,'var $iter'+$loop_num+'='+iterable.to_js())
new_nodes.push(new_node)
new_node=new $Node('expression')
var js='for(var $i'+$loop_num+'=0;$i'+$loop_num
js +='<$iter'+$loop_num+'.__len__();$i'+$loop_num+'++)'
new $NodeJSCtx(new_node,js)
new_nodes.push(new_node)
var children=node.children
node.parent.children.splice(rank,1)
for(var i=new_nodes.length-1;i>=0;i--){
node.parent.insert(rank,new_nodes[i])
}
var new_node=new $Node('expression')
node.insert(0,new_node)
var C=new $NodeCtx(new_node)
var target_expr=new $ExprCtx(C,'left',true)
target_expr.tree=target.tree
var assign=new $AssignCtx(target_expr)
assign.tree[1]=new $JSCode('$iter'+$loop_num+'.__item__($i'+$loop_num+')')
node.parent.children[rank+1].children=children
$loop_num++
}
this.to_js=function(){
var iterable=this.tree.pop()
return 'for '+$to_js(this.tree)+' in '+iterable.to_js()
}
}
function $FromCtx(C){
this.type='from'
this.parent=C
this.names=[]
C.tree.push(this)
this.expect='module'
this.toString=function(){return '(from) '+this.module+' (import) '+this.names + '(parent module)' + this.parent_module}
this.to_js=function(){return '$import_from("'+this.module+'",'+this.names+', "' + this.parent_module +'");\n'}
}
function $FuncArgs(C){
this.type='func_args'
this.parent=C
this.tree=[]
C.tree.push(this)
this.toString=function(){return 'func args '+this.tree}
this.expect='id'
this.has_default=false
this.has_star_arg=false
this.has_kw_arg=false
this.to_js=function(){return $to_js(this.tree)}
}
function $FuncArgIdCtx(C,name){
this.type='func_arg_id'
this.name=name
this.parent=C
this.tree=[]
C.tree.push(this)
this.toString=function(){return 'func arg id '+this.name +'='+this.tree}
this.expect='='
this.to_js=function(){return this.name+$to_js(this.tree)}
}
function $FuncStarArgCtx(C,op){
this.type='func_star_arg'
this.op=op
this.parent=C
C.tree.push(this)
this.toString=function(){return '(func star arg '+this.op+') '+this.name}
}
function $GlobalCtx(C){
this.type='global'
this.parent=C
this.tree=[]
C.tree.push(this)
this.expect='id'
this.toString=function(){return 'global '+this.tree}
this.transform=function(node,rank){
var scope=$get_scope(this)
if(scope.globals===undefined){scope.globals=[]}
for(var i=0;i<this.tree.length;i++){
scope.globals.push(this.tree[i].value)
}
}
this.to_js=function(){return ''}
}
function $IdCtx(C,value,minus){
this.type='id'
this.toString=function(){return '(id) '+this.value+':'+(this.tree||'')}
this.value=value
this.minus=minus
this.parent=C
this.tree=[]
C.tree.push(this)
this.to_js=function(){
var val=this.value
if(['print','alert','eval','open'].indexOf(this.value)>-1){val='$'+val}
return val+$to_js(this.tree,'')
}
}
function $ImportCtx(C){
this.type='import'
this.toString=function(){return 'import '+this.tree}
this.parent=C
this.tree=[]
C.tree.push(this)
this.expect='id'
this.to_js=function(){
return '$import_list(['+$to_js(this.tree)+'])'
}
}
function $ImportedModuleCtx(C,name){
this.toString=function(){return ' (imported module) '+this.name}
this.parent=C
this.name=name
this.alias=name
C.tree.push(this)
this.to_js=function(){
return '["'+this.name+'","'+this.alias+'"]'
}
}
function $IntCtx(C,value){
this.type='int'
this.value=value
this.toString=function(){return 'int '+this.value}
this.parent=C
this.tree=[]
C.tree.push(this)
this.to_js=function(){return 'Number('+this.value+')'}
}
function $JSCode(js){
this.js=js
this.toString=function(){return this.js}
this.to_js=function(){return this.js}
}
function $KwArgCtx(C){
this.type='kwarg'
this.toString=function(){return 'kwarg '+this.tree[0]+'='+this.tree[1]}
this.parent=C.parent
this.tree=[C.tree[0]]
C.parent.tree.pop()
C.parent.tree.push(this)
this.to_js=function(){
var res='$Kw("'+this.tree[0].to_js()+'",'
res +=$to_js(this.tree.slice(1,this.tree.length))+')'
return res
}
}
function $LambdaCtx(C){
this.type='lambda'
this.toString=function(){return '(lambda) '+this.args_start+' '+this.body_start}
this.parent=C
C.tree.push(this)
this.tree=[]
this.to_js=function(){
var ctx_node=this
while(ctx_node.parent!==undefined){ctx_node=ctx_node.parent}
var module=ctx_node.node.module
var src=document.$py_src[module]
var qesc=new RegExp('"',"g")
var args=src.substring(this.args_start,this.body_start).replace(qesc,'\\"')
var body=src.substring(this.body_start+1,this.body_end).replace(qesc,'\\"')
return '$lambda("'+args+'","'+body+'")'
}
}
function $ListOrTupleCtx(C,real){
this.type='list_or_tuple'
this.start=$pos
this.real=real
this.expect='id'
this.closed=false
this.toString=function(){
if(this.real==='list'){return '(list) ['+this.tree+']'}
else if(this.real==='list_comp'){return '(list comp) ['+this.intervals+'-'+this.tree+']'}
else{return '(tuple) ('+this.tree+')'}
}
this.parent=C
this.tree=[]
C.tree.push(this)
this.to_js=function(){
if(this.real==='list'){return '['+$to_js(this.tree)+']'}
else if(this.real==='list_comp'||this.real==='gen_expr'){
var res_env=[],local_env=[],env=[]
var ctx_node=this
while(ctx_node.parent!==undefined){ctx_node=ctx_node.parent}
var module=ctx_node.node.module
var src=document.$py_src[module]
for(var i=0;i<this.expression.length;i++){
var ids=$get_ids(this.expression[i])
for(var i=0;i<ids.length;i++){
if(res_env.indexOf(ids[i])===-1){res_env.push(ids[i])}
}
}
var comp=this.tree[0]
for(var i=0;i<comp.tree.length;i++){
var elt=comp.tree[i]
if(elt.type==='comp_for'){
var target_list=elt.tree[0]
for(var j=0;j<target_list.tree.length;j++){
var name=target_list.tree[j].value
if(local_env.indexOf(name)===-1){
local_env.push(name)
}
}
var comp_iter=elt.tree[1].tree[0]
var ids=$get_ids(comp_iter)
for(var i=0;i<ids.length;i++){
if(env.indexOf(ids[i])===-1){env.push(ids[i])}
}
}else if(elt.type==="comp_if"){
var if_expr=elt.tree[0]
var ids=$get_ids(if_expr)
for(var i=0;i<ids.length;i++){
if(env.indexOf(ids[i])===-1){env.push(ids[i])}
}
}
}
for(var i=0;i<res_env.length;i++){
if(local_env.indexOf(res_env[i])===-1){
env.push(res_env[i])
}
}
var res='{'
for(var i=0;i<env.length;i++){
res +="'"+env[i]+"':"+env[i]
if(i<env.length-1){res+=','}
}
res +='},'
var qesc=new RegExp('"',"g")
for(var i=1;i<this.intervals.length;i++){
var txt=src.substring(this.intervals[i-1],this.intervals[i]).replace(qesc,'\\"')
txt=txt.replace(/\n/g,' ')
res +='"'+txt+'"'
if(i<this.intervals.length-1){res+=','}
}
if(this.real==='list_comp'){return '$list_comp('+res+')'}
else{return '$gen_expr('+res+')'}
}else if(this.real==='tuple'){
if(this.tree.length===1 && this.has_comma===undefined){return this.tree[0].to_js()}
else{return 'tuple('+$to_js(this.tree)+')'}
}
}
}
function $NodeCtx(node){
this.node=node
node.C=this
this.tree=[]
this.type='node'
this.toString=function(){return 'node '+this.tree}
this.to_js=function(){
if(this.tree.length>1){
var new_node=new $Node('expression')
var ctx=new $NodeCtx(new_node)
ctx.tree=[this.tree[1]]
new_node.indent=node.indent+4
this.tree.pop()
node.add(new_node)
}
return $to_js(this.tree)
}
}
function $NodeJSCtx(node,js){
this.node=node
node.C=this
this.type='node_js'
this.tree=[js]
this.toString=function(){return 'js '+js}
this.to_js=function(){return js}
}
function $NotCtx(C){
this.type='not'
this.parent=C
this.tree=[]
C.tree.push(this)
this.toString=function(){return 'not ('+this.tree+')'}
this.to_js=function(){return '!bool('+$to_js(this.tree)+')'}
}
function $OpCtx(C,op){
this.type='op'
this.op=op
this.toString=function(){return '(op '+this.op+')'+this.tree}
this.parent=C.parent
this.tree=[C]
C.parent.tree.pop()
C.parent.tree.push(this)
this.to_js=function(){
if(this.op==='and'){
var res='$test_expr($test_item('+this.tree[0].to_js()+')&&'
res +='$test_item('+this.tree[1].to_js()+'))'
return res
}else if(this.op==='or'){
var res='$test_expr($test_item('+this.tree[0].to_js()+')||'
res +='$test_item('+this.tree[1].to_js()+'))'
return res
}else{
var res=this.tree[0].to_js()
if(this.op==="is"){
res +='==='+this.tree[1].to_js()
}else{
res +='.__'+$operators[this.op]+'__('+this.tree[1].to_js()+')'
}
return res
}
}
}
function $ParentClassCtx(C){
this.type='parent_class'
this.expect='id'
this.toString=function(){return '('+this.tree+')'}
this.parent=C
this.tree=[]
C.tree.push(this)
}
function $PassCtx(C){
this.type='pass'
this.toString=function(){return '(pass)'}
this.parent=C
this.tree=[]
C.tree.push(this)
this.to_js=function(){return 'void(0)'}
}
function $RaiseCtx(C){
this.type='raise'
this.toString=function(){return ' (raise) '+this.tree}
this.parent=C
this.tree=[]
C.tree.push(this)
this.to_js=function(){
if(this.tree.length===0){return '$raise()'}
var exc=this.tree[0]
if(exc.type==='id'){return 'throw '+exc.value+'("")'}
else{return 'throw '+$to_js(this.tree)}
}
}
function $ReturnCtx(C){
this.type='return'
this.toString=function(){return 'return '+this.tree}
this.parent=C
this.tree=[]
C.tree.push(this)
this.to_js=function(){return 'return '+$to_js(this.tree)}
}
function $SingleKwCtx(C,token){
this.type='single_kw'
this.token=token
this.parent=C
this.tree=[]
C.tree.push(this)
this.toString=function(){return this.token}
this.to_js=function(){return this.token}
}
function $StarArgCtx(C){
this.type='star_arg'
this.parent=C
this.tree=[]
C.tree.push(this)
this.toString=function(){return '(star arg) '+this.tree}
this.to_js=function(){
return '$ptuple('+$to_js(this.tree)+')'
}
}
function $StringCtx(C,value){
this.type='str'
this.value=value
this.toString=function(){return 'string '+this.value+' '+(this.tree||'')}
this.parent=C
this.tree=[]
C.tree.push(this)
this.to_js=function(){
return this.value.replace(/\n/g,' \\\n')+$to_js(this.tree,'')
}
}
function $SubCtx(C){
this.type='sub'
this.func='getitem' 
this.toString=function(){return '(sub) '+this.tree}
this.value=C.tree[0]
C.tree.pop()
C.tree.push(this)
this.parent=C
this.tree=[]
this.to_js=function(){
var res=this.value.to_js()+'.__'+this.func+'__('
if(this.tree.length===1){
return res+this.tree[0].to_js()+')'
}else{
res +='slice('
for(var i=0;i<this.tree.length;i++){
if(this.tree[i].type==='abstract_expr'){res+='null'}
else{res+=this.tree[i].to_js()}
if(i<this.tree.length-1){res+=','}
}
return res+'))'
}
}
}
function $TargetCtx(C,name){
this.toString=function(){return ' (target) '+this.name}
this.parent=C
this.name=name
this.alias=null
C.tree.push(this)
this.to_js=function(){
return '["'+this.name+'","'+this.alias+'"]'
}
}
function $TargetListCtx(C){
this.type='target_list'
this.parent=C
this.tree=[]
this.expect='id'
C.tree.push(this)
this.toString=function(){return '(target list) '+this.tree}
}
function $TernaryCtx(C){
this.type='ternary'
this.parent=C.parent
C.parent.tree.pop()
C.parent.tree.push(this)
C.parent=this
this.tree=[C]
this.toString=function(){return '(ternary) '+this.tree}
this.to_js=function(){
var env='{'
var ids=$get_ids(this)
for(var i=0;i<ids.length;i++){
env +='"'+ids[i]+'":'+ids[i]
if(i<ids.length-1){env+=','}
}
env+='}'
var qesc=new RegExp('"',"g")
var args='"'+this.tree[1].to_js().replace(qesc,'\\"')+'","' 
args +=this.tree[0].to_js().replace(qesc,'\\"')+'","' 
args +=this.tree[2].to_js().replace(qesc,'\\"')
return '$ternary('+env+','+args+'")'
}
}
function $TryCtx(C){
this.type='try'
this.parent=C
C.tree.push(this)
this.toString=function(){return '(try) '}
this.transform=function(node,rank){
if(node.parent.children.length===rank+1){
$_SyntaxError(C,"missing clause after 'try' 1")
}else{
var next_ctx=node.parent.children[rank+1].C.tree[0]
if(['except','finally'].indexOf(next_ctx.type)===-1){
$_SyntaxError(C,"missing clause after 'try' 2")
}
}
new $NodeJSCtx(node,'try')
var catch_node=new $Node('expression')
new $NodeJSCtx(catch_node,'catch($err'+$loop_num+')')
node.parent.insert(rank+1,catch_node)
var new_node=new $Node('expression')
new $NodeJSCtx(new_node,'if(false){void(0)}')
catch_node.insert(0,new_node)
var pos=rank+2
var has_default=false 
var has_else=false 
while(true){
if(pos===node.parent.children.length){break}
var ctx=node.parent.children[pos].C.tree[0]
if(ctx.type==='except'||
(ctx.type==='single_kw' && ctx.token==='finally')){
if(has_else){$_SyntaxError("'except' or 'finally' after 'else'")}
ctx.error_name='$err'+$loop_num
if(ctx.tree.length>0 && ctx.tree[0].alias!==null){
var new_node=new $Node('expression')
var js='var '+ctx.tree[0].alias+'='+ctx.tree[0].name
js +='($err'+$loop_num+'.message)'
new $NodeJSCtx(new_node,js)
node.parent.children[pos].insert(0,new_node)
}
catch_node.insert(catch_node.children.length,
node.parent.children[pos])
if(ctx.type==='except' && ctx.tree.length===0){
if(has_default){$_SyntaxError(C,'more than one except: line')}
has_default=true
}
node.parent.children.splice(pos,1)
}else if(ctx.type==='single_kw' && ctx.token==='else'){
if(has_else){$_SyntaxError(C,"more than one 'else'")}
has_else=true
var else_children=node.parent.children[pos].children
for(var i=0;i<else_children.length;i++){
node.add(else_children[i])
}
node.parent.children.splice(pos,1)
}else{break}
}
if(!has_default){
var new_node=new $Node('expression')
new $NodeJSCtx(new_node,'else{throw $err'+$loop_num+'}')
catch_node.insert(catch_node.children.length,new_node)
}
$loop_num++
}
this.to_js=function(){return 'try'}
}
function $UnaryCtx(C,op){
this.type='unary'
this.op=op
this.toString=function(){return '(unary) '+this.op+' ['+this.tree+']'}
this.parent=C
this.tree=[]
C.tree.push(this)
this.to_js=function(){return this.op+$to_js(this.tree)}
}
function $YieldCtx(C){
this.type='yield'
this.toString=function(){return '(yield) '+this.tree}
this.parent=C
this.tree=[]
C.tree.push(this)
this.transform=function(node,rank){
if(this.transformed!==undefined){return}
var scope=$get_scope(node.C.tree[0])
scope.C.tree[0].type='generator'
this.transformed=true
this.func_name=scope.C.tree[0].name
scope.C.tree[0].add_generator_declaration()
}
this.to_js=function(){
return '$'+this.func_name+'.$iter.push('+$to_js(this.tree)+')'
}
}
var $loop_num=0
var $iter_num=0 
function $add_line_num(node,rank){
if(node.type==='module'){
var i=0
while(i<node.children.length){
i +=$add_line_num(node.children[i],i)
}
}else{
var elt=node.C.tree[0],offset=1
var flag=true
if(node.line_num===undefined){flag=false}
if(elt.type==='condition' && elt.token==='elif'){flag=false}
else if(elt.type==='except'){flag=false}
else if(elt.type==='single_kw'){flag=false}
if(flag){
js='document.$line_info=['+node.line_num+',"'+node.module+'"]'
var new_node=new $Node('expression')
new $NodeJSCtx(new_node,js)
node.parent.insert(rank,new_node)
offset=2
}
var i=0
while(i<node.children.length){
i +=$add_line_num(node.children[i],i)
}
return offset
}
}
function $augmented_assign(C,op){
var assign=new $AssignCtx(C)
var new_op=new $OpCtx(C,op.substr(0,op.length-1))
assign.tree.push(new_op)
C.parent.tree.pop()
C.parent.tree.push(assign)
return new_op
}
function $get_scope(C){
var ctx_node=C.parent
while(ctx_node.type!=='node'){ctx_node=ctx_node.parent}
var tree_node=ctx_node.node
var scope=null
while(tree_node.parent.type!=='module'){
var ntype=tree_node.parent.C.tree[0].type
if(['def','class'].indexOf(ntype)>-1){
scope=tree_node.parent
scope.ntype=ntype
break
}
tree_node=tree_node.parent
}
return scope
}
function $get_ids(ctx){
var res=[]
if(ctx.type==='expr' &&
ctx.tree[0].type==='list_or_tuple' &&
ctx.tree[0].real==='list_comp'){return[]}
if(ctx.type==='id'){res.push(ctx.value)}
else if(ctx.type==='attribute'||ctx.type==='sub'){
var res1=$get_ids(ctx.value)
for(var i=0;i<res1.length;i++){
if(res.indexOf(res1[i])===-1){res.push(res1[i])}
}
}else if(ctx.type==='call'){
var res1=$get_ids(ctx.func)
for(var i=0;i<res1.length;i++){
if(res.indexOf(res1[i])===-1){res.push(res1[i])}
}
}
if(ctx.tree!==undefined){
for(var i=0;i<ctx.tree.length;i++){
var res1=$get_ids(ctx.tree[i])
for(var j=0;j<res1.length;j++){
if(res.indexOf(res1[j])===-1){
res.push(res1[j])
}
}
}
}
return res
}
function $to_js(tree,sep){
if(sep===undefined){sep=','}
var res=''
for(var i=0;i<tree.length;i++){
if(tree[i].to_js!==undefined){
res +=tree[i].to_js()
}else{
throw Error('no to_js() for '+tree[i])
}
if(i<tree.length-1){res+=sep}
}
return res
}
var $expr_starters=['id','int','float','str','[','(','{','not','lambda']
function $arbo(ctx){
while(ctx.parent!=undefined){ctx=ctx.parent}
return ctx
}
function $transition(C,token){
if(C.type==='abstract_expr'){
if($expr_starters.indexOf(token)>-1){
C.parent.tree.pop()
var commas=C.with_commas
C=C.parent
}
if(token==='id'){return new $IdCtx(new $ExprCtx(C,'id',commas),arguments[2])}
else if(token==='str'){return new $StringCtx(new $ExprCtx(C,'str',commas),arguments[2])}
else if(token==='int'){return new $IntCtx(new $ExprCtx(C,'int',commas),arguments[2])}
else if(token==='float'){return new $FloatCtx(new $ExprCtx(C,'float',commas),arguments[2])}
else if(token==='('){return new $ListOrTupleCtx(new $ExprCtx(C,'tuple',commas),'tuple')}
else if(token==='['){return new $ListOrTupleCtx(new $ExprCtx(C,'list',commas),'list')}
else if(token==='{'){return new $DictOrSetCtx(new $ExprCtx(C,'dict_or_set',commas))}
else if(token==='not'){return new $NotCtx(new $ExprCtx(C,'not',commas))}
else if(token==='lambda'){return new $LambdaCtx(new $ExprCtx(C,'lambda',commas))}
else if(token==='op' && '+-'.search(arguments[2])){
return new $UnaryCtx(C,arguments[2])
}else if(token==='='){$_SyntaxError(C,token)}
else{return $transition(C.parent,token,arguments[2])}
}else if(C.type==='assert'){
if($expr_starters.indexOf(token)>-1&&C.expect===undefined){
C.expect='cond'
return $transition(new $AbstractExprCtx(C,false),token,arguments[2])
}else if(token===',' && C.expect==='cond'){
C.expect='arg'
return C
}else if($expr_starters.indexOf(token)>-1 && C.expect==='arg'){
return $transition(new $AbstractExprCtx(C,false),token,arguments[2])
}else if(token==='eol' && C.expect){
return $transition(C.parent,token)
}else{$_SyntaxError(C,token)}
}else if(C.type==='assign'){
if(token==='eol'){return $transition(C.parent,'eol')}
else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='attribute'){
if(token==='id'){
var name=arguments[2]
if(name.substr(0,2)=='$$'){name=name.substr(2)}
C.name=name
return C.parent
}else{$_SyntaxError(C,token)}
}else if(C.type==='call'){
if(token===','){return C}
else if($expr_starters.indexOf(token)>-1){
var expr=new $CallArgCtx(C)
return $transition(expr,token,arguments[2])
}else if(token===')'){return C.parent}
else if(token==='op'){
var op=arguments[2]
if(op==='-'){return new $UnaryCtx(C,'-')}
else if(op==='+'){return C}
else if(op==='*'){return new $StarArgCtx(C)}
else if(op==='**'){return new $DoubleStarArgCtx(C)}
else{throw Error('SyntaxError')}
}else{return $transition(C.parent,token,arguments[2])}
}else if(C.type==='call_arg'){
if($expr_starters.indexOf(token)>-1 && C.expect==='id'){
C.expect=','
var expr=new $AbstractExprCtx(C,false)
return $transition(expr,token,arguments[2])
}else if(token==='=' && C.expect===','){
return new $ExprCtx(new $KwArgCtx(C),'kw_value',false)
}else if(token==='op' && C.expect==='id'){
var op=arguments[2]
C.expect=','
if(op==='+'||op==='-'){
return $transition(new $AbstractExprCtx(C,false),token,op)
}else if(op==='*'){C.expect=',';return new $StarArgCtx(C)}
else if(op==='**'){C.expect=',';return new $DoubleStarArgCtx(C)}
else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(token===')' && C.expect===','){
return $transition(C.parent,token)
}else if(token===','&& C.expect===','){
return new $CallArgCtx(C.parent)
}else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='class'){
if(token==='id' && C.expect==='id'){
C.name=arguments[2]
C.expect='(:'
return C
}
else if(token==='(' && C.expect==='(:'){
return new $ParentClassCtx(C)
}else if(token===':' && C.expect==='(:'){return C.parent}
else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='comp_if'){
return $transition(C.parent,token,arguments[2])
}else if(C.type==='comp_for'){
if(token==='in' && C.expect==='in'){
C.expect=null
return new $AbstractExprCtx(new $CompIterableCtx(C),true)
}else if(C.expect===null){
return $transition(C.parent,token,arguments[2])
}else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='comp_iterable'){
return $transition(C.parent,token,arguments[2])
}else if(C.type==='comprehension'){
if(token==='if'){return new $AbstractExprCtx(new $CompIfCtx(C),false)}
else if(token==='for'){return new $TargetListCtx(new $CompForCtx(C))}
else{return $transition(C.parent,token,arguments[2])}
}else if(C.type==='condition'){
if(token===':'){
var new_node=new $Node('expression')
C.parent.node.add(new_node)
return new $NodeCtx(new_node)
}
else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='decorator'){
if(token==='id' && C.tree.length===0){
return $transition(new $AbstractExprCtx(C,false),token,arguments[2])
}else if(token==='eol'){return $transition(C.parent,token)}
else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='def'){
if(token==='id'){
if(C.name){
$_SyntaxError(C,'token '+token+' after '+C)
}else{
C.name=arguments[2]
return C
}
}else if(token==='('){return new $FuncArgs(C)}
else if(token===':'){return C.parent}
else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='dict_or_set'){
if(C.closed){
if(token==='['){return new $SubCtx(C)}
else if(token==='('){return new $CallArgCtx(new $CallCtx(C))}
else if(token==='op'){
return new $AbstractExprCtx(new $OpCtx(C,arguments[2]),false)
}else{return $transition(C.parent,token,arguments[2])}
}else{
if(C.expect===','){
if(token==='}'){
if((C.real==='set')||
(C.real==='dict'&&C.tree.length%2===0)){
C.items=C.tree
C.tree=[]
C.closed=true
return C
}else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(token===','){
if(C.real==='dict_or_set'){C.real='set'}
if(C.real==='dict' && C.tree.length%2){
$_SyntaxError(C,'token '+token+' after '+C)
}
C.expect='id'
return C
}else if(token===':'){
if(C.real==='dict_or_set'){C.real='dict'}
if(C.real==='dict'){
C.expect='id'
return C
}else{$_SyntaxError(C,'token '+token+' after '+C)}
}else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.expect==='id'){
if(token==='}'&&C.tree.length===0){
C.items=[]
C.tree=[]
C.closed=true
C.real='dict'
return C
}else if($expr_starters.indexOf(token)>-1){
C.expect=','
var expr=new $AbstractExprCtx(C,false)
return $transition(expr,token,arguments[2])
}else{$_SyntaxError(C,'token '+token+' after '+C)}
}else{return $transition(C.parent,token,arguments[2])}
}
}else if(C.type==='double_star_arg'){
if($expr_starters.indexOf(token)>-1){
return $transition(new $AbstractExprCtx(C,false),token,arguments[2])
}else if(token===','){return C.parent}
else if(token===')'){return $transition(C.parent,token)}
else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='except'){
if(token==='id' && C.expect==='id'){
new $TargetCtx(C,arguments[2])
C.expect='as'
return C
}else if(token==='as' && C.expect==='as'
&& C.has_alias===undefined 
&& C.tree.length===1){
C.expect='alias'
C.has_alias=true
return C
}else if(token==='id' && C.expect==='alias'){
if(C.parenth!==undefined){C.expect=','}
else{C.expect=':'}
C.tree[C.tree.length-1].alias=arguments[2]
return C
}else if(token===':' &&['id','as',':'].indexOf(C.expect)>-1){
return C.parent
}else if(token==='(' && C.expect==='id' && C.tree.length===0){
C.parenth=true
return C
}else if(token===')' &&[',','as'].indexOf(C.expect)>-1){
C.expect=':'
return C
}else if(token===',' && C.parenth!==undefined &&
C.has_alias===undefined &&
['as',','].indexOf(C.expect)>-1){
C.expect='id'
return C
}else{$_SyntaxError(C,'token '+token+' after '+C.expect)}
}else if(C.type==='expr'){
if($expr_starters.indexOf(token)>-1 && C.expect==='expr'){
C.expect=','
return $transition(new $AbstractExprCtx(C,false),token,arguments[2])
}else if(token==='not'&&C.expect===','){
return new $ExprNot(C)
}else if(token==='in'&&C.expect===','){
return new $AbstractExprCtx(new $OpCtx(C,'in'),false)
}else if(token===',' && C.expect===','){
if(C.with_commas){
C.expect='expr'
return C
}else{return $transition(C.parent,token)}
}else if(token==='.'){return new $AttrCtx(C)}
else if(token==='['){return new $AbstractExprCtx(new $SubCtx(C),false)}
else if(token==='('){return new $CallCtx(C)}
else if(token==='op'){
var op_parent=C.parent,op=arguments[2]
var op1=C.parent,repl=null
while(true){
if(op1.type==='expr'){op1=op1.parent}
else if(op1.type==='op'&&$op_weight[op1.op]>$op_weight[op]){repl=op1;op1=op1.parent}
else{break}
}
if(repl===null){
C.parent.tree.pop()
var expr=new $ExprCtx(op_parent,'operand',C.with_commas)
expr.expect=','
C.parent=expr
var new_op=new $OpCtx(C,op)
return new $AbstractExprCtx(new_op,false)
}
repl.parent.tree.pop()
var expr=new $ExprCtx(repl.parent,'operand',false)
expr.tree=[op1]
repl.parent=expr
var new_op=new $OpCtx(repl,op)
return new $AbstractExprCtx(new_op,false)
}else if(token==='augm_assign' && C.expect===','){
return $augmented_assign(C,arguments[2])
}else if(token==='=' && C.expect===','){
if(C.parent.type==="call_arg"){
return new $AbstractExprCtx(new $KwArgCtx(C),true)
}else{
while(C.parent!==undefined){C=C.parent}
C=C.tree[0]
return new $AbstractExprCtx(new $AssignCtx(C),true)
}
}else if(token==='if' && C.parent.type!=='comp_iterable'){
return new $AbstractExprCtx(new $TernaryCtx(C),false)
}else{return $transition(C.parent,token)}
}else if(C.type==='expr_not'){
if(token==='in'){
C.parent.tree.pop()
return new $AbstractExprCtx(new $OpCtx(C.parent,'not_in'),false)
}else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='for'){
if(token==='in'){return new $AbstractExprCtx(C,true)}
else if(token===':'){return C.parent}
else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='from'){
if(token==='id' && C.expect==='module'){
C.module=arguments[2]
C.expect='import'
return C
}else if(token==='import' && C.expect==='import'){
C.expect='id'
return C
}else if(token==='import' && C.expect==='module' 
&& C.relpath !==undefined){
C.expect='id'
return C
}else if(token==='id' && C.expect==='id'){
C.names.push(arguments[2])
C.expect=','
return C
}else if(token==='op' && arguments[2]==='*' 
&& C.expect==='id'
&& C.names.length===0){
C.names.push(arguments[2])
C.expect='eol'
return C
}else if(token===',' && C.expect===','){
C.expect='id'
return C
}else if(token==='eol' && 
(C.expect===',' || C.expect==='eol')){
return $transition(C.parent,token)
}else if(token==='.' && C.expect==='module'){
C.expect='module'
C.parent_module=C.parent.node.module
return C
}else if(token==='(' && C.expect==='id'){
C.expect='id'
return C
}else if(token===')' && C.expect===','){
C.expect='eol'
return C
}else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='func_arg_id'){
if(token==='=' && C.expect==='='){
C.parent.has_default=true
return new $AbstractExprCtx(C,false)
}else if(token===',' || token===')'){
if(C.parent.has_default && C.tree.length==0){
throw Error('SyntaxError: non-default argument follows default argument')
}else{
return $transition(C.parent,token)
}
}else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='func_args'){
if(token==='id' && C.expect==='id'){
C.expect=','
return new $FuncArgIdCtx(C,arguments[2])
}else if(token===','){
if(C.has_kw_arg){throw Error('SyntaxError')}
else if(C.expect===','){
C.expect='id'
return C
}else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(token===')'){
if(C.expect===','){return C.parent}
else if(C.tree.length==0){return C.parent}
else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(token==='op'){
var op=arguments[2]
C.expect=','
if(op=='*'){return new $FuncStarArgCtx(C,'*')}
else if(op=='**'){return new $FuncStarArgCtx(C,'**')}
else{$_SyntaxError(C,'token '+op+' after '+C)}
}else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='func_star_arg'){
if(token==='id' && C.name===undefined){
C.name=arguments[2]
return C.parent
}else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='global'){
if(token==='id' && C.expect==='id'){
new $IdCtx(C,arguments[2])
C.expect=','
return C
}else if(token===',' && C.expect===','){
C.expect='id'
return C
}else if(token==='eol' && C.expect===','){
return $transition(C.parent,token)
}else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='id'){
if(token==='='){
if(C.parent.type==='expr' &&
C.parent.parent !==undefined &&
C.parent.parent.type==='call_arg'){
return new $AbstractExprCtx(new $KwArgCtx(C.parent),false)
}else{return $transition(C.parent,token,arguments[2])}
}else if(token==='op'){return $transition(C.parent,token,arguments[2])}
else if(token=='id'){$_SyntaxError(C,'token '+token+' after '+C)}
else{return $transition(C.parent,token,arguments[2])}
}else if(C.type==='import'){
if(token==='id' && C.expect==='id'){
new $ImportedModuleCtx(C,arguments[2])
C.expect=','
return C
}else if(token===',' && C.expect===','){
C.expect='id'
return C
}else if(token==='as' && C.expect===','){
C.expect='alias'
return C
}else if(token==='id' && C.expect==='alias'){
C.expect=','
C.tree[C.tree.length-1].alias=arguments[2]
var mod_name=C.tree[C.tree.length-1].name
document.$py_module_alias[mod_name]=arguments[2]
return C
}else if(token==='eol' && C.expect===','){
return $transition(C.parent,token)
}else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='int'||C.type==='float'){
if($expr_starters.indexOf(token)>-1){
$_SyntaxError(C,'token '+token+' after '+C)
}else{return $transition(C.parent,token,arguments[2])}
}else if(C.type==='kwarg'){
if(token===')'){return $transition(C.parent,token)}
else if(token===','){return new $CallArgCtx(C.parent)}
else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==="lambda"){
if(C.args_start===undefined){
C.args_start=$pos
return C
}else if(token===':' && C.tree.length===0){
C.body_start=$pos
return new $AbstractExprCtx(C,false)
}else if(C.tree.length>0){
C.body_end=$pos
return $transition(C.parent,token)
}else if(C.tree.length===0){return C}
else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='list_or_tuple'){
if(C.closed){
if(token==='['){return new $SubCtx(C.parent)}
else if(token==='('){return new $CallCtx(C)}
else if(token==='.'){return new $AttrCtx(C)}
else if(token==='op'){
return new $AbstractExprCtx(new $OpCtx(C,arguments[2]),false)
}else{return $transition(C.parent,token,arguments[2])}
}else{
if(C.expect===','){
if((C.real==='tuple'||C.real==='gen_expr')
&& token===')'){
C.closed=true
if(C.real==='gen_expr'){C.intervals.push($pos)}
return C
}else if((C.real==='list'||C.real==='list_comp')
&& token===']'){
C.closed=true
if(C.real==='list_comp'){C.intervals.push($pos)}
return C
}else if(token===','){
if(C.real==='tuple'){C.has_comma=true}
C.expect='id'
return C
}else if(token==='for'){
if(C.real==='list'){C.real='list_comp'}
else{C.real='gen_expr'}
C.intervals=[C.start+1]
C.expression=C.tree
C.tree=[]
var comp=new $ComprehensionCtx(C)
return new $TargetListCtx(new $CompForCtx(comp))
}else{return $transition(C.parent,token,arguments[2])}
}else if(C.expect==='id'){
if(C.real==='tuple' && token===')'){
C.closed=true
return C
}else if(C.real==='list'&& token===']'){
C.closed=true
return C
}else if(token !==')'&&token!==']'&&token!==','){
C.expect=','
var expr=new $AbstractExprCtx(C,false)
return $transition(expr,token,arguments[2])
}
}else{return $transition(C.parent,token,arguments[2])}
}
}else if(C.type==='list_comp'){
if(token===']'){return C.parent}
else if(token==='in'){return new $ExprCtx(C,'iterable',true)}
else if(token==='if'){return new $ExprCtx(C,'condition',true)}
else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='node'){
if($expr_starters.indexOf(token)>-1){
var expr=new $AbstractExprCtx(C,true)
return $transition(expr,token,arguments[2])
}else if(token==='class'){return new $ClassCtx(C)}
else if(token==='def'){return new $DefCtx(C)}
else if(token==='for'){return new $TargetListCtx(new $ForExpr(C))}
else if(['if','elif','while'].indexOf(token)>-1){
return new $AbstractExprCtx(new $ConditionCtx(C,token),false)
}else if(['else','finally'].indexOf(token)>-1){
return new $SingleKwCtx(C,token)
}else if(token==='try'){return new $TryCtx(C)}
else if(token==='except'){return new $ExceptCtx(C)}
else if(token==='assert'){return new $AssertCtx(C)}
else if(token==='from'){return new $FromCtx(C)}
else if(token==='import'){return new $ImportCtx(C)}
else if(token==='global'){return new $GlobalCtx(C)}
else if(token==='lambda'){return new $LambdaCtx(C)}
else if(token==='pass'){return new $PassCtx(C)}
else if(token==='raise'){return new $RaiseCtx(C)}
else if(token==='return'){
var ret=new $ReturnCtx(C)
return new $AbstractExprCtx(ret,true)
}else if(token==='yield'){
var yield=new $YieldCtx(C)
return new $AbstractExprCtx(yield,true)
}else if(token==='del'){return new $AbstractExprCtx(new $DelCtx(C),true)}
else if(token==='@'){return new $DecoratorCtx(C)}
else if(token===':'){
var tree_node=C.node
var new_node=new $Node('expression')
tree_node.add(new_node)
return new $NodeCtx(new_node)
}else if(token==='eol'){
if(C.tree.length===0){
C.node.parent.children.pop()
return C.node.parent.C
}
return C
}else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='not'){
if(token==='in'){
C.parent.parent.tree.pop()
return new $ExprCtx(new $OpCtx(C.parent,'not_in'),'op',false)
}else if($expr_starters.indexOf(token)>-1){
var expr=new $AbstractExprCtx(C,false)
return $transition(expr,token,arguments[2])
}else{return $transition(C.parent,token)}
}else if(C.type==='op'){
if($expr_starters.indexOf(token)>-1){
return $transition(new $AbstractExprCtx(C,false),token,arguments[2])
}else if(token==='op' && '+-'.search(arguments[2])>-1){
return new $UnaryCtx(C,arguments[2])
}else{return $transition(C.parent,token)}
}else if(C.type==='parent_class'){
if(token==='id' && C.expect==='id'){
new $IdCtx(C,arguments[2])
C.expect=','
return C
}else if(token===',' && C.expect==','){
C.expect='id'
return C
}else if(token===')'){return C.parent}
else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='pass'){
if(token==='eol'){return C.parent}
else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='raise'){
if(token==='id' && C.tree.length===0){
return new $IdCtx(new $ExprCtx(C,'exc',false),arguments[2])
}else if(token==='eol'){
return $transition(C.parent,token)
}else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='return'){
return $transition(C.parent,token)
}else if(C.type==='single_kw'){
if(token===':'){return C.parent}
else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='star_arg'){
if($expr_starters.indexOf(token)>-1){
return $transition(new $AbstractExprCtx(C,false),token,arguments[2])
}else if(token===','){return C.parent}
else if(token===')'){return $transition(C.parent,token)}
else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='str'){
if(token==='['){return new $AbstractExprCtx(new $SubCtx(C),false)}
else if(token==='('){return new $CallCtx(C)}
else if(token=='str'){C.value +='+'+arguments[2];return C}
else{return $transition(C.parent,token,arguments[2])}
}else if(C.type==='sub'){
if($expr_starters.indexOf(token)>-1){
var expr=new $AbstractExprCtx(C,false)
return $transition(expr,token,arguments[2])
}else if(token===']'){return C.parent}
else if(token===':'){
return new $AbstractExprCtx(C,false)
}else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='target_list'){
if(token==='id' && C.expect==='id'){
C.expect=','
new $IdCtx(C,arguments[2])
return C
}else if((token==='('||token==='[')&&C.expect==='id'){
C.expect=','
return new $TargetListCtx(C)
}else if((token===')'||token===']')&&C.expect===','){
return C.parent
}else if(token===',' && C.expect==','){
C.expect='id'
return C
}else if(C.expect===','){return $transition(C.parent,token,arguments[2])}
else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='ternary'){
if(token==='else'){return new $AbstractExprCtx(C,false)}
else{return $transition(C.parent,token,arguments[2])}
}else if(C.type==='try'){
if(token===':'){return C.parent}
else{$_SyntaxError(C,'token '+token+' after '+C)}
}else if(C.type==='unary'){
if(['int','float'].indexOf(token)>-1){
C.parent.tree.pop()
var value=arguments[2]
if(C.op==='-'){value=-value}
return $transition(C.parent,token,value)
}else if(token==='id'){
C.parent.tree.pop()
if(C.op==='-'){
var int_expr=new $IntCtx(C.parent,-1)
return $transition(new $OpCtx(int_expr,'*'),token,arguments[2])
}else{
return $transition(C.parent,token,arguments[2])
}
}else if(token==="op" && '+-'.search(arguments[2])>-1){
var op=arguments[2]
if(C.op===op){C.op='+'}else{C.op='-'}
return C
}else{return $transition(C.parent,token,arguments[2])}
}else if(C.type==='yield'){
return $transition(C.parent,token)
}
}
__BRYTHON__.py2js=function(src,module){
src=src.replace(/\r\n/gm,'\n')
while(src.length>0 &&(src.charAt(0)=="\n" || src.charAt(0)=="\r")){
src=src.substr(1)
}
if(src.charAt(src.length-1)!="\n"){src+='\n'}
if(module===undefined){module='__main__'}
document.$py_src[module]=src 
var root=$tokenize(src,module)
root.transform()
if(document.$debug>0){$add_line_num(root,null,module)}
return root
}
function $tokenize(src,module){
var delimiters=[["#","\n","comment"],['"""','"""',"triple_string"],
["'","'","string"],['"','"',"string"],
["r'","'","raw_string"],['r"','"',"raw_string"]]
var br_open={"(":0,"[":0,"{":0}
var br_close={")":"(","]":"[","}":"{"}
var br_stack=""
var br_pos=new Array()
var kwdict=["class","return",
"for","lambda","try","finally","raise","def","from",
"nonlocal","while","del","global","with",
"as","elif","else","if","yield","assert","import",
"except","raise","in","not","pass",
]
var unsupported=["nonlocal","with"]
var $indented=['class','def','for','condition','single_kw','try','except']
var forbidden=['case','catch','debugger','default','delete',
'do','function','instanceof','new','switch','this','throw',
'typeof','var','void','with','enum','export','extends','super',
'Anchor','Area','arguments','Array','assign','blur','Boolean','Button',
'callee','caller','captureEvents','Checkbox','clearInterval','clearTimeout',
'close','closed','constructor','Date','defaultStatus','document','Document',
'Element','escape','FileUpload','find','focus','Form','Frame','Frames','Function',
'getClass','Hidden','history','History','home','Image','Infinity','InnerHeight',
'InnerWidth','isFinite','isNan','java','JavaArray','JavaClass','JavaObject',
'JavaPackage','length','Link','location','Location','locationbar','Math','menubar',
'MimeType','moveBy','moveTo','name','NaN','navigate','navigator','Navigator','netscape',
'Number','Object','onBlur','onError','onFocus','onLoad','onUnload','opener',
'Option','outerHeight','OuterWidth','Packages','pageXoffset','pageYoffset',
'parent','parseFloat','parseInt','Password','personalbar','Plugin','prototype',
'Radio','ref','RegExp','releaseEvents','Reset','resizeBy','resizeTo','routeEvent',
'scroll','scrollbars','scrollBy','scrollTo','Select','self','setInterval','setTimeout',
'status','statusbar','stop','String','Submit','sun','taint','Text','Textarea','toolbar',
'top','toString','unescape','untaint','unwatch','valueOf','watch','window','Window'
]
var punctuation={',':0,':':0}
var int_pattern=new RegExp("^\\d+")
var float_pattern1=new RegExp("^\\d+\\.\\d*(e-?\\d+)?")
var float_pattern2=new RegExp("^\\d+(e-?\\d+)")
var id_pattern=new RegExp("[\\$_a-zA-Z]\\w*")
var qesc=new RegExp('"',"g")
var C=null
var root=new $Node('module')
root.indent=-1
var new_node=new $Node('expression')
current=root
var name=""
var _type=null
var pos=0
indent=null
var lnum=1
while(pos<src.length){
var flag=false
var car=src.charAt(pos)
if(indent===null){
var indent=0
while(pos<src.length){
if(src.charAt(pos)==" "){indent++;pos++}
else if(src.charAt(pos)=="\t"){
indent++;pos++
while(indent%8>0){indent++}
}else{break}
}
if(src.charAt(pos)=='\n'){pos++;lnum++;indent=null;continue}
else if(src.charAt(pos)==='#'){
var offset=src.substr(pos).search(/\n/)
if(offset===-1){break}
pos+=offset+1;lnum++;indent=null;continue
}
new_node.indent=indent
new_node.line_num=lnum
new_node.module=module
if(indent>current.indent){
if(C!==null){
if($indented.indexOf(C.tree[0].type)==-1){
$IndentationError(module,'unexpected indent',pos)
}
}
current.add(new_node)
}else{
while(indent!==current.indent){
current=current.parent
if(current===undefined || indent>current.indent){
$IndentationError(module,'unexpected indent',pos)
}
}
current.parent.add(new_node)
}
current=new_node
C=new $NodeCtx(new_node)
continue
}
if(car=="#"){
var end=src.substr(pos+1).search('\n')
if(end==-1){end=src.length-1}
pos +=end+1;continue
}
if(car=='"' || car=="'"){
var raw=false
var end=null
if(name.length>0 && name.toLowerCase()=="r"){
raw=true;name=""
}
if(src.substr(pos,3)==car+car+car){_type="triple_string";end=pos+3}
else{_type="string";end=pos+1}
var escaped=false
var zone=car
var found=false
while(end<src.length){
if(escaped){zone+=src.charAt(end);escaped=false;end+=1}
else if(src.charAt(end)=="\\"){
if(raw){
zone +='\\\\'
end++
}else{
if(src.charAt(end+1)=='\n'){
end +=2
lnum++
}else{
zone+=src.charAt(end);escaped=true;end+=1
}
}
}else if(src.charAt(end)==car){
if(_type=="triple_string" && src.substr(end,3)!=car+car+car){
end++
}else{
found=true
$pos=pos-zone.length-1
var string=zone.substr(1).replace(qesc,'\\"')
C=$transition(C,'str',zone+car)
pos=end+1
if(_type=="triple_string"){pos=end+3}
break
}
}else{
zone +=src.charAt(end)
if(src.charAt(end)=='\n'){lnum++}
end++
}
}
if(!found){$_SyntaxError(C,"String end not found")}
continue
}
if(name==""){
if(car.search(/[a-zA-Z_]/)!=-1){
name=car 
pos++;continue
}
}else{
if(car.search(/\w/)!=-1){
name+=car
pos++;continue
}else{
if(kwdict.indexOf(name)>-1){
if(unsupported.indexOf(name)>-1){
$_SyntaxError(C,"Unsupported Python keyword '"+name+"'")
}
$pos=pos-name.length
C=$transition(C,name)
}else if(name in $operators){
$pos=pos-name.length
C=$transition(C,'op',name)
}else{
if(forbidden.indexOf(name)>-1){name='$$'+name}
$pos=pos-name.length
C=$transition(C,'id',name)
}
name=""
continue
}
}
if(car=="."){
$pos=pos
C=$transition(C,'.')
pos++;continue
}
if(car.search(/\d/)>-1){
var res=float_pattern1.exec(src.substr(pos))
if(res){
if(res[0].search('e')>-1){
$pos=pos
C=$transition(C,'float',res[0])
}else{
$pos=pos
C=$transition(C,'float',eval(res[0]))
}
}else{
res=float_pattern2.exec(src.substr(pos))
if(res){
$pos=pos
C=$transition(C,'float',res[0])
}else{
res=int_pattern.exec(src.substr(pos))
$pos=pos
C=$transition(C,'int',eval(res[0]))
}
}
pos +=res[0].length
continue
}
if(car=="\n"){
lnum++
if(br_stack.length>0){
pos++;continue
}else{
if(current.C.tree.length>0){
$pos=pos
C=$transition(C,'eol')
indent=null
new_node=new $Node()
}else{
new_node.line_num=lnum
}
pos++;continue
}
}
if(car in br_open){
br_stack +=car
br_pos[br_stack.length-1]=[C,pos]
$pos=pos
C=$transition(C,car)
pos++;continue
}
if(car in br_close){
if(br_stack==""){
$_SyntaxError(C,"Unexpected closing bracket")
}else if(br_close[car]!=$last(br_stack)){
$_SyntaxError(C,"Unbalanced bracket",pos)
}else{
br_stack=br_stack.substr(0,br_stack.length-1)
$pos=pos
C=$transition(C,car)
pos++;continue
}
}
if(car=="="){
if(src.charAt(pos+1)!="="){
$pos=pos
C=$transition(C,'=')
pos++;continue
}else{
$pos=pos
C=$transition(C,'op','==')
pos+=2;continue
}
}
if(car in punctuation){
$pos=pos
C=$transition(C,car)
pos++;continue
}
if(car in $first_op_letter){
var op_match=""
for(op_sign in $operators){
if(op_sign==src.substr(pos,op_sign.length)
&& op_sign.length>op_match.length){
op_match=op_sign
}
}
$pos=pos
if(op_match.length>0){
if(op_match in $augmented_assigns){
C=$transition(C,'augm_assign',op_match)
}else{
C=$transition(C,'op',op_match)
}
pos +=op_match.length
continue
}
}
if(car=='\\' && src.charAt(pos+1)=='\n'){
lnum++;pos+=2;continue
}
if(car=='@'){
$pos=pos
C=$transition(C,car)
pos++;continue
}
if(car!=' '&&car!=='\t'){$pos=pos;$_SyntaxError(C,'unknown token ['+car+']')}
pos +=1
}
if(br_stack.length!=0){
var br_err=br_pos[0]
$pos=br_err[1]
$_SyntaxError(br_err[0],"Unbalanced bracket "+br_stack.charAt(br_stack.length-1))
}
return root
}
function brython(debug){
document.$py_src={}
document.$py_module_path={}
document.$py_module_alias={}
document.$py_next_hash=-Math.pow(2,53)
document.$debug=debug
document.$exc_stack=[]
var elts=document.getElementsByTagName("script")
var href=window.location.href
var href_elts=href.split('/')
href_elts.pop()
var script_path=href_elts.join('/')
__BRYTHON__.path=[script_path]
for(var $i=0;$i<elts.length;$i++){
var elt=elts[$i]
if(elt.type=="text/python"){
if(elt.src!==''){
if(window.XMLHttpRequest){
var $xmlhttp=new XMLHttpRequest()
}else{
var $xmlhttp=new ActiveXObject("Microsoft.XMLHTTP")
}
$xmlhttp.onreadystatechange=function(){
var state=this.readyState
if(state===4){
src=$xmlhttp.responseText
}
}
$xmlhttp.open('GET',elt.src,false)
$xmlhttp.send()
document.$py_module_path['__main__']=elt.src 
__BRYTHON__.path=[elt.src]
}else{
var src=(elt.innerHTML || elt.textContent)
document.$py_module_path['__main__']='.' 
}
var root=__BRYTHON__.py2js(src,'__main__')
var js=root.to_js()
if(debug===2){console.log(js)}
eval(js)
}else{
var br_scripts=['brython.js','py_list.js']
for(var j=0;j<br_scripts.length;j++){
var bs=br_scripts[j]
if(elt.src.substr(elt.src.length-bs.length)==bs){
if(elt.src.length===bs.length ||
elt.src.charAt(elt.src.length-bs.length-1)=='/'){
var path=elt.src.substr(0,elt.src.length-bs.length)
__BRYTHON__.brython_path=path
__BRYTHON__.path.push(path+'Lib')
break
}
}
}
}
}
}
function $MakeArgs($fname,$args,$required,$defaults,$other_args,$other_kw){
var i=null,$PyVars={},$def_names=[],$ns={}
for(var k in $defaults){$def_names.push(k);$ns[k]=$defaults[k]}
if($other_args !=null){$ns[$other_args]=[]}
if($other_kw !=null){$dict_keys=[];$dict_values=[]}
var upargs=[]
for(var i=0;i<$args.length;i++){
if($args[i]===null){upargs.push(null)}
else if(isinstance($args[i],$ptuple)){
for(var j=0;j<$args[i].arg.length;j++){
upargs.push($args[i].arg[j])
}
}else if(isinstance($args[i],$pdict)){
for(var j=0;j<$args[i].arg.$keys.length;j++){
upargs.push($Kw($args[i].arg.$keys[j],$args[i].arg.$values[j]))
}
}else{
upargs.push($args[i])
}
}
for(var $i=0;$i<upargs.length;$i++){
$arg=upargs[$i]
$PyVar=$JS2Py($arg)
if(isinstance($arg,$Kw)){
$PyVar=$arg.value
if($arg.name in $PyVars){
throw new TypeError($fname+"() got multiple values for argument '"+$arg.name+"'")
}else if($required.indexOf($arg.name)>-1){
var ix=$required.indexOf($arg.name)
eval('var '+$required[ix]+"=$PyVar")
$ns[$required[ix]]=$PyVar
}else if($arg.name in $defaults){
$ns[$arg.name]=$PyVar
}else if($other_kw!=null){
$dict_keys.push($arg.name)
$dict_values.push($PyVar)
}else{
throw new TypeError($fname+"() got an unexpected keyword argument '"+$arg.name+"'")
}
if($arg.name in $defaults){delete $defaults[$arg.name]}
}else{
if($i<$required.length){
eval('var '+$required[$i]+"=$PyVar")
$ns[$required[$i]]=$PyVar
}else if($i<$required.length+$def_names.length){
$ns[$def_names[$i-$required.length]]=$PyVar
}else if($other_args!=null){
eval('$ns["'+$other_args+'"].push($PyVar)')
}else{
msg=$fname+"() takes "+$required.length+' positional arguments '
msg +='but more were given'
throw TypeError(msg)
}
}
}
if($other_kw!=null){$ns[$other_kw]=new $DictClass($dict_keys,$dict_values)}
return $ns
}
function $list_comp(){
var $env=arguments[0]
for(var $arg in $env){
eval("var "+$arg+'=$env["'+$arg+'"]')
}
var $res='res'+Math.random().toString(36).substr(2,8)
var $py=$res+"=[]\n"
var indent=0
for(var i=2;i<arguments.length;i++){
for(var j=0;j<indent;j++){$py +=' '}
$py +=arguments[i]+':\n'
indent +=4
}
for(var j=0;j<indent;j++){$py +=' '}
$py +=$res+'.append('+arguments[1]+')'
var $js=__BRYTHON__.py2js($py).to_js()
eval($js)
return eval($res)
}
function $generator(func){
var res=function(){
func.$iter=[]
func.apply(this,arguments)
var obj=new Object()
obj.__class__=$generator
obj.__len__=function(){return func.$iter.__len__()}
obj.__item__=function(rank){return func.$iter.__item__(rank)}
return obj
}
res.__str__=function(){return "<function "+res.__name__+">"}
return res
}
function $ternary(env,cond,expr1,expr2){
for(var attr in env){eval('var '+attr+'=env["'+attr+'"]')}
var res='if ('+cond+'){\n'
res +='    var $res = '+expr1+'\n}else{\n'
res +='    var $res = '+expr2+'\n}'
eval(res)
return $res
}
function $lambda(args,body){
var $res='res'+Math.random().toString(36).substr(2,8)
var $py='def '+$res+'('+args+'):\n'
$py +='    return '+body
var $js=__BRYTHON__.py2js($py).to_js()
eval($js)
return eval($res)
}
function $JS2Py(src){
if(src===null){return None}
if(typeof src==='number'){
if(src%1===0){return src}
else{return float(src)}
}
if(src.__class__!==undefined){return src}
if(typeof src=="object"){
if(src.constructor===Array){return src}
else if($isNode(src)){return $DOMNode(src)}
else if($isEvent(src)){return $DOMEvent(src)}
}
return JSObject(src)
}
function $module(){}
$module.__class__=$type
$module.__str__=function(){return "<class 'module'>"}
function $getattr(obj,attr){
if(obj[attr]!==undefined){
var res=obj[attr]
if(typeof res==="function"){
res=$bind(res, obj)
}
return $JS2Py(res)
}
}
function $bind(func, thisValue){
return function(){return func.apply(thisValue, arguments)}
}
function $raise(){
if(document.$exc_stack.length>0){throw $last(document.$exc_stack)}
else{throw Error('Exception')}
}
function $src_error(name,module,msg,pos){
var pos2line={}
var lnum=1
var src=document.$py_src[module]
var line_pos={1:0}
for(i=0;i<src.length;i++){
pos2line[i]=lnum
if(src.charAt(i)=='\n'){lnum+=1;line_pos[lnum]=i}
}
var line_num=pos2line[pos]
var lines=src.split('\n')
info="\nmodule '"+module+"' line "+line_num
info +='\n'+lines[line_num-1]+'\n'
var lpos=pos-line_pos[line_num]
for(var i=0;i<lpos;i++){info+=' '}
info +='^'
err=new Error()
err.name=name
err.__name__=name
err.message=msg
err.info=info
err.py_error=true
if(document.$stderr!==null){document.$stderr_buff=err.message}
throw err
}
function $SyntaxError(module,msg,pos){
$src_error('SyntaxError',module,msg,pos)
}
function $IndentationError(module,msg,pos){
$src_error('IndentationError',module,msg,pos)
}
function $resolve_attr(obj,factory,attr){
if(obj[attr]!==undefined){return obj[attr]}
if(factory[attr]!==undefined){
var res=factory[attr]
if(typeof res==='function'){
res=(function(func){
return function(){
var args=[obj]
for(var i=0;i<arguments.length;i++){args.push(arguments[i])}
return func.apply(obj,args)
}
})(res)
res.__str__=(function(x){
return function(){
var res="<bound method "+factory.__name__+'.'+x
res +=' of '+obj.__str__()+'>'
return res
}
})(attr)
}
return res
}else{
for(var i=0;i<factory.parents.length;i++){
try{
return $resolve_attr(obj,factory.parents[i],attr)
}catch(err){
console.log(err)
}
}
throw AttributeError('object has no attribute '+attr)
}
}
function $class_constructor(class_name,factory){
var parent_classes=[]
for(var i=2;i<arguments.length;i++){
parent_classes.push(arguments[i])
}
factory.parents=parent_classes
factory.__name__=class_name
var f=function(){
var obj=new Object()
obj.__class__=f
for(var attr in factory){
if(attr.substr(0,2)!=='__'){continue}
if(typeof factory[attr]==="function"){
var func=factory[attr]
obj[attr]=(function(func){
return function(){
var args=[obj]
for(var i=0;i<arguments.length;i++){args.push(arguments[i])}
return func.apply(obj,args)
}
})(func)
obj[attr].__str__=(function(x){
return function(){
var res="<bound method "+class_name+'.'+x
res +=' of '+obj.__str__()+'>'
return res
}
})(attr)
}else{obj[attr]=factory[attr]}
}
obj.__getattr__=function(attr){
return $resolve_attr(obj,factory,attr)
}
obj.__setattr__=function(attr,value){obj[attr]=value}
if(obj.__str__===undefined){
obj.__str__=function(){
return "<object '"+class_name+"'>"
}
}
obj.toString=obj.__str__
if(factory.__init__ !==undefined){
var args=[obj]
for(var i=0;i<arguments.length;i++){args.push(arguments[i])}
factory.__init__.apply(obj,args)
}
return obj
}
f.__str__=function(){return "<class '"+class_name+"'>"}
for(var attr in factory){
f[attr]=factory[attr]
f[attr].__str__=(function(x){
return function(){return "<function "+class_name+'.'+x+'>'}
})(attr)
}
f.__getattr__=function(attr){
if(f[attr]!==undefined){return f[attr]}
return factory[attr]
}
f.__setattr__=function(attr,value){factory[attr]=value}
return f
}
var $dq_regexp=new RegExp('"',"g")
function $escape_dq(arg){return arg.replace($dq_regexp,'\\"')}
document.$stderr={'write':function(data){void(0)}}
document.$stderr_buff='' 
document.$stdout={
write: function(data){console.log(data)}
}
function $type(){}
$type.__class__=$type
$type.toString=function(){return "<class 'type'>"}
function $UnsupportedOpType(op,class1,class2){
$raise('TypeError',
"unsupported operand type(s) for "+op+": '"+class1+"' and '"+class2+"'")
}
function $KwClass(name,value){
this.__class__=$Kw
this.name=name
this.value=value
}
$KwClass.prototype.toString=function(){
return '<kw '+this.name+' : '+this.value.toString()+'>'
}
function $Kw(name,value){
return new $KwClass(name,value)
}
function $ptuple_class(arg){
this.__class__=$ptuple
this.arg=arg
}
function $ptuple(arg){return new $ptuple_class(arg)}
function $pdict_class(arg){
this.__class__=$pdict
this.arg=arg
}
function $pdict(arg){return new $pdict_class(arg)}
function $test_item(expr){
document.$test_result=expr
return bool(expr)
}
function $test_expr(){
return document.$test_result
}
Function.prototype.__eq__=function(other){
if(typeof other !=='function'){return False}
return other+''===this+''
}
Function.prototype.__class__=Function
Function.prototype.__str__=function(){return "<function "+this.__name__+">"}
Array.prototype.match=function(other){
var $i=0
while($i<this.length && $i<other.length){
if(this[$i]!==other[$i]){return false}
$i++
}
return true
}
if(!Array.indexOf){
Array.prototype.indexOf=function(obj){
for(var i=0;i<this.length;i++){
if(this[i]==obj){
return i;
}
}
return -1;
}
}
try{console}
catch(err){
console={'log':function(data){void(0)}}
}
function $List2Dict(){
var res={}
var i=0
if(arguments.length==1 && arguments[0].constructor==Array){
for(i=0;i<arguments[0].length;i++){
res[arguments[0][i]]=0
}
}else{
for(i=0;i<arguments.length;i++){
res[arguments[i]]=0
}
}
return res
}
function $last(item){
if(typeof item=="string"){return item.charAt(item.length-1)}
else if(typeof item=="object"){return item[item.length-1]}
}
function $XmlHttpClass(obj){
this.__class__='XMLHttpRequest'
this.__getattr__=function(attr){
if('get_'+attr in this){return this['get_'+attr]()}
else{return obj[attr]}
}
this.get_text=function(){return obj.responseText}
this.get_xml=function(){return $DomObject(obj.responseXML)}
this.get_headers=function(){return list(obj.getAllResponseHeaders().split('\n'))}
this.get_get_header=function(){
var reqobj=obj
return function(header){return reqobj.getResponseHeader(header)}
}
}
function Ajax(){}
Ajax.__class__=$type
Ajax.__str__=function(){return "<class 'Ajax'>"}
function $AjaxClass(){
if(window.XMLHttpRequest){
var $xmlhttp=new XMLHttpRequest()
}else{
var $xmlhttp=new ActiveXObject("Microsoft.XMLHTTP")
}
$xmlhttp.$ajax=this
$xmlhttp.$requestTimer=null
$xmlhttp.onreadystatechange=function(){
var state=this.readyState
var req=this.$ajax
var timer=this.$requestTimer
var obj=new $XmlHttpClass($xmlhttp)
if(state===0 && 'on_uninitialized' in req){req.on_uninitialized(obj)}
else if(state===1 && 'on_loading' in req){req.on_loading(obj)}
else if(state===2 && 'on_loaded' in req){req.on_loaded(obj)}
else if(state===3 && 'on_interactive' in req){req.on_interactive(obj)}
else if(state===4 && 'on_complete' in req){
if(timer !==null){window.clearTimeout(timer)}
req.on_complete(obj)
}
}
this.__class__=Ajax
this.__getattr__=function(attr){return $getattr(this,attr)}
this.__setattr__=function(attr,value){setattr(this,attr,value)}
this.__str__=function(){return "<object 'Ajax'>"}
this.open=function(method,url,async){
$xmlhttp.open(method,url,async)
}
this.set_header=function(key,value){
$xmlhttp.setRequestHeader(key,value)
}
this.send=function(params){
if(!params || params.$keys.length==0){$xmlhttp.send();return}
if(!isinstance(params,dict)){$raise('TypeError',
"send() argument must be dictonary, not '"+str(params.__class__)+"'")}
var res=''
for(i=0;i<params.$keys.length;i++){
res +=encodeURIComponent(str(params.$keys[i]))+'='+encodeURIComponent(str(params.$values[i]))+'&'
}
res=res.substr(0,res.length-1)
$xmlhttp.send(res)
}
this.set_timeout=function(seconds,func){
$xmlhttp.$requestTimer=setTimeout(
function(){$xmlhttp.abort();func()}, 
seconds*1000);
}
}
function ajax(){
return new $AjaxClass()
}
function $getMouseOffset(target, ev){
ev=ev || window.event
var docPos=$getPosition(target)
var mousePos=$mouseCoords(ev)
return{x:mousePos.x - docPos.x, y:mousePos.y - docPos.y}
}
function $getPosition(e){
var left=0
var top=0
var width=e.offsetWidth
var height=e.offsetHeight
while(e.offsetParent){
left +=e.offsetLeft
top +=e.offsetTop
e=e.offsetParent
}
left +=e.offsetLeft
top +=e.offsetTop
return{left:left, top:top, width:width, height:height}
}
function $mouseCoords(ev){
var posx=0
var posy=0
if(!ev)var ev=window.event
if(ev.pageX || ev.pageY){
posx=ev.pageX
posy=ev.pageY
}else if(ev.clientX || ev.clientY){
posx=ev.clientX + document.body.scrollLeft
+ document.documentElement.scrollLeft
posy=ev.clientY + document.body.scrollTop
+ document.documentElement.scrollTop
}
var res=object()
res.x=int(posx)
res.y=int(posy)
res.__getattr__=function(attr){return this[attr]}
res.__class__="MouseCoords"
return res
}
var $DOMNodeAttrs=['nodeName','nodeValue','nodeType','parentNode',
'childNodes','firstChild','lastChild','previousSibling','nextSibling',
'attributes','ownerDocument']
function $isNode(obj){
for(var i=0;i<$DOMNodeAttrs.length;i++){
if(obj[$DOMNodeAttrs[i]]===undefined){return false}
}
return true
}
var $DOMEventAttrs_W3C=['NONE','CAPTURING_PHASE','AT_TARGET','BUBBLING_PHASE',
'type','target','currentTarget','eventPhase','bubbles','cancelable','timeStamp',
'stopPropagation','preventDefault','initEvent']
var $DOMEventAttrs_IE=['altKey','altLeft','button','cancelBubble',
'clientX','clientY','contentOverflow','ctrlKey','ctrlLeft','data',
'dataFld','dataTransfer','fromElement','keyCode','nextPage',
'offsetX','offsetY','origin','propertyName','reason','recordset',
'repeat','screenX','screenY','shiftKey','shiftLeft',
'source','srcElement','srcFilter','srcUrn','toElement','type',
'url','wheelDelta','x','y']
function $isEvent(obj){
flag=true
for(var i=0;i<$DOMEventAttrs_W3C.length;i++){
if(obj[$DOMEventAttrs_W3C[i]]===undefined){flag=false;break}
}
if(flag){return true}
for(var i=0;i<$DOMEventAttrs_IE.length;i++){
if(obj[$DOMEventAttrs_IE[i]]===undefined){return false}
}
return true
}
function DOMObject(){}
DOMObject.__class__=$type
DOMObject.__str__=function(){return "<class 'DOMObject'>"}
DOMObject.toString=function(){return "<class 'DOMObject'>"}
$DOMtoString=function(){
var res="<DOMObject object type '" 
return res+$NodeTypes[this.nodeType]+"' name '"+this.nodeName+"'>"
}
$NodeTypes={1:"ELEMENT",
2:"ATTRIBUTE",
3:"TEXT",
4:"CDATA_SECTION",
5:"ENTITY_REFERENCE",
6:"ENTITY",
7:"PROCESSING_INSTRUCTION",
8:"COMMENT",
9:"DOCUMENT",
10:"DOCUMENT_TYPE",
11:"DOCUMENT_FRAGMENT",
12:"NOTATION"
}
function DOMEvent(){}
DOMEvent.__class__=$type
DOMEvent.toString=function(){return "<class 'DOMEvent'>"}
function $DOMEvent(ev){
ev.__class__=DOMEvent
ev.__getattr__=function(attr){
if(attr=="x"){return $mouseCoords(ev).x}
if(attr=="y"){return $mouseCoords(ev).y}
if(attr=="data"){return new $Clipboard(ev.dataTransfer)}
return $getattr(ev,attr)
}
if(ev.preventDefault===undefined){ev.preventDefault=function(){ev.returnValue=false}}
if(ev.stopPropagation===undefined){ev.stopPropagation=function(){ev.cancelBubble=true}}
ev.__str__=function(){return '<DOMEvent object>'}
ev.toString=ev.__str__
return ev
}
function $Clipboard(data){
this.data=data
this.__class__="Clipboard"
}
$Clipboard.prototype.__getitem__=function(name){
return this.data.getData(name)
}
$Clipboard.prototype.__setitem__=function(name,value){
this.data.setData(name,value)
}
$Clipboard.prototype.__setattr__=function(attr,value){
eval("this.data."+attr+"=value")
}
function $OpenFile(file,mode,encoding){
this.reader=new FileReader()
if(mode==='r'){this.reader.readAsText(file,encoding)}
else if(mode==='rb'){this.reader.readAsBinaryString(file)}
this.file=file
this.__class__=dom.FileReader
this.__getattr__=function(attr){
if(this['get_'+attr]!==undefined){return this['get_'+attr]}
return this.reader[attr]
}
this.__setattr__=(function(obj){
return function(attr,value){
if(attr.substr(0,2)=='on'){
if(window.addEventListener){
var callback=function(ev){return value($DOMEvent(ev))}
obj.addEventListener(attr.substr(2),callback)
}else if(window.attachEvent){
var callback=function(ev){return value($DOMEvent(window.event))}
obj.attachEvent(attr,callback)
}
}else if('set_'+attr in obj){return obj['set_'+attr](value)}
else if(attr in obj){obj[attr]=value}
else{setattr(obj,attr,value)}
}
})(this.reader)
}
dom={File : function(){},
FileReader : function(){}
}
dom.File.__class__=$type
dom.File.__str__=function(){return "<class 'File'>"}
dom.FileReader.__class__=$type
dom.FileReader.__str__=function(){return "<class 'FileReader'>"}
function $OptionsClass(parent){
this.parent=parent
this.__getattr__=function(attr){
if('get_'+attr in this){return eval('this.get_'+attr)}
if(attr in this.parent.elt.options){
var obj=eval('this.parent.options.'+attr)
if((typeof obj)=='function'){
throw AttributeError("'options' object has no attribute '"+attr+'"')
}
return $JS2Py(obj)
}
}
this.__class__='options'
this.__getitem__=function(key){
return $DOMNode(parent.options[key])
}
this.__delitem__=function(arg){
parent.options.remove(arg)
}
this.__len__=function(){return parent.options.length}
this.__setattr__=function(attr,value){
parent.options[attr]=value
}
this.__setitem__=function(attr,value){
parent.options[attr]=$JS2Py(value)
}
this.get_append=function(element){
parent.options.add(element)
}
this.get_insert=function(index,element){
if(index===undefined){parent.options.add(element)}
else{parent.options.add(element,index)}
}
this.get_item=function(index){
return parent.options.item(index)
}
this.get_namedItem=function(name){
return parent.options.namedItem(name)
}
this.get_remove=function(arg){parent.options.remove(arg)}
}
function $Location(){
var obj=new object()
for(var x in window.location){obj[x]=window.location[x]}
obj.__class__=new $class(this,'Location')
obj.toString=function(){return window.location.toString()}
return obj
}
function JSObject(obj){
return new $JSObject(obj)
}
JSObject.__class__=$type
JSObject.__str__=function(){return "<class 'JSObject'>"}
JSObject.toString=JSObject.__str__
function $JSObject(js){
this.js=js
this.__class__=JSObject
this.__str__=function(){return "<object 'JSObject' wraps "+this.js+">"}
this.toString=this.__str__
}
$JSObject.prototype.__bool__=function(){return new Boolean(this.js)}
$JSObject.prototype.__getitem__=function(rank){
if(this.js.item!==undefined){return this.js.item(rank)}
else{throw AttributeError,this+' has no attribute __getitem__'}
}
$JSObject.prototype.__item__=function(rank){
if(this.js.item!==undefined){return this.js.item(rank)}
else{throw AttributeError,this+' has no attribute __item__'}
}
$JSObject.prototype.__len__=function(){
if(this.js.length!==undefined){return this.js.length}
else{throw AttributeError,this+' has no attribute __len__'}
}
$JSObject.prototype.__getattr__=function(attr){
var obj=this
if(obj.js[attr]!==undefined){
var obj=this.js,obj_attr=this.js[attr]
if(typeof this.js[attr]=='function'){
return function(){
var args=[]
for(var i=0;i<arguments.length;i++){args.push(arguments[i])}
var res=obj_attr.apply(obj,args)
if(typeof res=='object'){return new $JSObject(res)}
else if(res===undefined){return None}
else{return $JS2Py(res)}
}
}else if(obj===window && attr==='location'){
return $Location()
}else{
return $JS2Py(this.js[attr])
}
}else{
throw AttributeError("no attribute "+attr)
}
}
$JSObject.prototype.__setattr__=function(attr,value){
if(isinstance(value,JSObject)){
this.js[attr]=value.js
}else{
this.js[attr]=value
}
}
function $Location(){
var obj=new object()
for(var x in window.location){obj[x]=window.location[x]}
obj.__class__=new $class(this,'Location')
obj.toString=function(){return window.location.toString()}
return obj
}
win=new $JSObject(window)
function DOMNode(){}
function $DOMNode(elt){
if(!('$brython_id' in elt)){
elt.$brython_id=Math.random().toString(36).substr(2, 8)
for(var attr in DOMNode.prototype){elt[attr]=DOMNode.prototype[attr]}
elt.__str__=$DOMtoString
elt.toString=elt.__str__
}
return elt
}
DOMNode.prototype.__add__=function(other){
var res=$TagSum()
res.children=[this]
if(isinstance(other,$TagSum)){
for(var $i=0;$i<other.children.length;$i++){res.children.push(other.children[$i])}
}else if(isinstance(other,[str,int,float,list,dict,set,tuple])){
res.children.push(document.createTextNode(str(other)))
}else{res.children.push(other)}
return res
}
DOMNode.prototype.__class__=DOMObject
DOMNode.prototype.__delitem__=function(key){
if(this.nodeType===9){
var res=document.getElementById(key)
if(res){res.parentNode.removeChild(res)}
else{throw KeyError(key)}
}else{
this.removeChild(this.childNodes[key])
}
}
DOMNode.prototype.__eq__=function(other){
if('isEqualNode' in this){return this.isEqualNode(other)}
else if('$brython_id' in this){return this.$brython_id===other.$brython_id}
else{throw NotImplementedError('__eq__ is not implemented')}
}
DOMNode.prototype.__getattr__=function(attr){
if('get_'+attr in this){return this['get_'+attr]()}
var res=this.getAttribute(attr)
if(res){return res}
return $getattr(this,attr)
}
DOMNode.prototype.__getitem__=function(key){
if(this.nodeType===9){
if(typeof key==="string"){
var res=document.getElementById(key)
if(res){return $DOMNode(res)}
else{throw KeyError(key)}
}else{
try{
var elts=document.getElementsByTagName(key.name),res=[]
for(var $i=0;$i<elts.length;$i++){res.push($DOMNode(elts[$i]))}
return res
}catch(err){
throw KeyError(str(key))
}
}
}else{
return $DOMNode(this.childNodes[key])
}
}
DOMNode.prototype.__in__=function(other){return other.__contains__(this)}
DOMNode.prototype.__item__=function(key){
return $DOMNode(this.childNodes[key])
}
DOMNode.prototype.__le__=function(other){
var obj=this
if(this.nodeType===9){obj=this.body}
if(isinstance(other,$TagSum)){
var $i=0
for($i=0;$i<other.children.length;$i++){
obj.appendChild(other.children[$i])
}
}else if(typeof other==="string" || typeof other==="number"){
var $txt=document.createTextNode(other.toString())
obj.appendChild($txt)
}else{
obj.appendChild(other)
}
}
DOMNode.prototype.__len__=function(){return this.childNodes.length}
DOMNode.prototype.__mul__=function(other){
if(isinstance(other,int)&& other.valueOf()>0){
var res=$TagSum()
for(var i=0;i<other.valueOf();i++){
var clone=this.get_clone()()
res.children.push(clone)
}
return res
}else{
throw ValueError("can't multiply "+this.__class__+"by "+other)
}
}
DOMNode.prototype.__ne__=function(other){return !this.__eq__(other)}
DOMNode.prototype.__radd__=function(other){
var res=$TagSum()
var txt=document.createTextNode(other)
res.children=[txt,this]
return res 
}
DOMNode.prototype.__setattr__=function(attr,value){
if(attr.substr(0,2)=='on'){
if(window.addEventListener){
var callback=function(ev){return value($DOMEvent(ev))}
this.addEventListener(attr.substr(2),callback)
}else if(window.attachEvent){
var callback=function(ev){return value($DOMEvent(window.event))}
this.attachEvent(attr,callback)
}
}else{
attr=attr.replace('_','-')
if('set_'+attr in this){return this['set_'+attr](value)}
var res=this.getAttribute(attr)
if(res!==undefined){this.setAttribute(attr,value)}
else if(attr in this){this[attr]=value}
else{setattr(this,attr,value)}
}
}
DOMNode.prototype.__setitem__=function(key,value){
this.childNodes[key]=value
}
DOMNode.prototype.get_get=function(){
if(this.getElementsByName!==undefined){
return function(){
var $ns=$MakeArgs('get',arguments,[],{},null,'kw')
if('$$name'.__in__($ns['kw'])){
var res=[]
var node_list=document.getElementsByName($ns['kw'].__getitem__('$$name'))
if(node_list.length===0){return[]}
for(var i=0;i<node_list.length;i++){
res.push($DOMNode(node_list[i]))
}
}
if('id'.__in__($ns['kw'])){
var id_res=document.getElementById($ns['kw'].__getitem__('id'))
if(!id_res){return[]}
else{
var elt=$DOMNode(id_res)
if(res===undefined){res=[elt]}
else{
flag=false
for(var i=0;i<res.length;i++){
if(elt.__eq__(res[i])){flag=true;break}
}
if(!flag){return[]}
}
}
}
if('selector'.__in__($ns['kw'])){
var node_list=document.querySelectorAll($ns['kw'].__getitem__('selector'))
var sel_res=[]
if(node_list.length===0){return[]}
for(var i=0;i<node_list.length;i++){
sel_res.push($DOMNode(node_list[i]))
}
if(res===undefined){return sel_res}
var to_delete=[]
for(var i=0;i<res.length;i++){
var elt=res[i]
flag=false
for(var j=0;j<sel_res.length;j++){
if(elt.__eq__(sel_res[j])){flag=true;break}
}
if(!flag){to_delete.push(i)}
}
for(var i=to_delete.length-1;i>=0;i--){
res.splice(to_delete[i],1)
}
return res
}
return res
}
}
}
DOMNode.prototype.get_clone=function(){
res=$DOMNode(this.cloneNode(true))
for(var attr in this){
if(attr.substr(0,2)=='on' && this[attr]!==undefined){
res[attr]=this[attr]
}
}
var func=function(){return res}
return func
}
DOMNode.prototype.get_remove=function(){
var obj=this
return function(child){obj.removeChild(child)}
}
DOMNode.prototype.get_getContext=function(){
if(!('getContext' in this)){throw AttributeError(
"object has no attribute 'getContext'")}
var obj=this
return function(ctx){return new $JSObject(obj.getContext(ctx))}
}
DOMNode.prototype.get_parent=function(){
if(this.parentElement){return $DOMNode(this.parentElement)}
else{return None}
}
DOMNode.prototype.get_options=function(){
return new $OptionsClass(this)
}
DOMNode.prototype.get_left=function(){
return int($getPosition(this)["left"])
}
DOMNode.prototype.get_top=function(){
return int($getPosition(this)["top"])
}
DOMNode.prototype.get_children=function(){
var res=[]
for(var i=0;i<this.childNodes.length;i++){
res.push($DOMNode(this.childNodes[i]))
}
return res
}
DOMNode.prototype.get_reset=function(){
var $obj=this
return function(){$obj.reset()}
}
DOMNode.prototype.get_style=function(){
return new $JSObject(this.style)
}
DOMNode.prototype.set_style=function(style){
for(var i=0;i<style.$keys.length;i++){
this.style[style.$keys[i]]=style.$values[i]
}
}
DOMNode.prototype.get_submit=function(){
var $obj=this
return function(){$obj.submit()}
}
DOMNode.prototype.get_text=function(){
return this.innerText || this.textContent
}
DOMNode.prototype.get_html=function(){return this.innerHTML}
DOMNode.prototype.get_value=function(value){return this.value}
DOMNode.prototype.set_html=function(value){this.innerHTML=str(value)}
DOMNode.prototype.set_text=function(value){
this.innerText=str(value)
this.textContent=str(value)
}
DOMNode.prototype.set_value=function(value){this.value=value.toString()}
doc=$DOMNode(document)
function $Tag(tagName,args){
var $i=null
var elt=null
var elt=$DOMNode(document.createElement(tagName))
elt.parent=this
if(args!=undefined && args.length>0){
$start=0
$first=args[0]
if(!isinstance($first,$Kw)){
$start=1
if(isinstance($first,[str,int,float])){
txt=document.createTextNode($first.toString())
elt.appendChild(txt)
}else if(isinstance($first,$TagSum)){
for($i=0;$i<$first.children.length;$i++){
elt.appendChild($first.children[$i])
}
}else{
try{elt.appendChild($first)}
catch(err){throw ValueError('wrong element '+$first)}
}
}
for($i=$start;$i<args.length;$i++){
$arg=args[$i]
if(isinstance($arg,$Kw)){
if($arg.name.toLowerCase().substr(0,2)==="on"){
eval('elt.'+$arg.name.toLowerCase()+'=function(){'+$arg.value+'}')
}else if($arg.name.toLowerCase()=="style"){
elt.set_style($arg.value)
}else{
if($arg.value!==false){
try{
elt.setAttribute($arg.name.toLowerCase(),$arg.value)
}catch(err){
throw ValueError("can't set attribute "+$arg.name)
}
}
}
}
}
}
return elt
}
function $TagSumClass(){
this.__class__=$TagSum
this.children=[]
}
$TagSumClass.prototype.appendChild=function(child){
this.children.push(child)
}
$TagSumClass.prototype.__add__=function(other){
if(isinstance(other,$TagSum)){
this.children=this.children.concat(other.children)
}else if(isinstance(other,str)){
this.children=this.children.concat(document.createTextNode(other))
}else{this.children.push(other)}
return this
}
$TagSumClass.prototype.__radd__=function(other){
var res=$TagSum()
res.children=this.children.concat(document.createTextNode(other))
return res
}
$TagSumClass.prototype.clone=function(){
var res=$TagSum(), $i=0
for($i=0;$i<this.children.length;$i++){
res.children.push(this.children[$i].cloneNode(true))
}
return res
}
function $TagSum(){
return new $TagSumClass()
}
function A(){return $Tag('A',arguments)}
var $src=A+'' 
$tags=['A', 'ABBR', 'ACRONYM', 'ADDRESS', 'APPLET',
'B', 'BDO', 'BIG', 'BLOCKQUOTE', 'BUTTON',
'CAPTION', 'CENTER', 'CITE', 'CODE',
'DEL', 'DFN', 'DIR', 'DIV', 'DL',
'EM', 'FIELDSET', 'FONT', 'FORM', 'FRAMESET',
'H1', 'H2', 'H3', 'H4', 'H5', 'H6',
'I', 'IFRAME', 'INS', 'KBD', 'LABEL', 'LEGEND',
'MAP', 'MENU', 'NOFRAMES', 'NOSCRIPT', 'OBJECT',
'OL', 'OPTGROUP', 'PRE', 'Q', 'S', 'SAMP',
'SCRIPT', 'SELECT', 'SMALL', 'SPAN', 'STRIKE',
'STRONG', 'STYLE', 'SUB', 'SUP', 'TABLE',
'TEXTAREA', 'TITLE', 'TT', 'U', 'UL',
'VAR', 'BODY', 'COLGROUP', 'DD', 'DT', 'HEAD',
'HTML', 'LI', 'P', 'TBODY','OPTION', 
'TD', 'TFOOT', 'TH', 'THEAD', 'TR',
'AREA', 'BASE', 'BASEFONT', 'BR', 'COL', 'FRAME',
'HR', 'IMG', 'INPUT', 'ISINDEX', 'LINK',
'META', 'PARAM']
$tags=$tags.concat(['ARTICLE','ASIDE','FIGURE','FOOTER','HEADER','NAV',
'SECTION','AUDIO','VIDEO','CANVAS','COMMAND','DATALIST',
'DETAILS','OUTPUT','PROGRESS','HGROUP','MARK','METER','TIME',
'RP','RT','RUBY'])
for($i=0;$i<$tags.length;$i++){
$code=$src.replace(/A/gm,$tags[$i])
eval($code)
eval($tags[$i]+'.name="'+$tags[$i]+'"')
}
function $LocalStorageClass(){
this.__class__='localStorage'
this.supported=typeof(Storage)!=="undefined"
this.__delitem__=function(key){
if(this.supported){localStorage.removeItem(key)}
else{$raise('NameError',"local storage is not supported by this browser")}
}
this.__getitem__=function(key){
if(this.supported){
res=localStorage[key]
if(res===undefined){return None}
else{return res}
}
else{$raise('NameError',"local storage is not supported by this browser")}
}
this.__setitem__=function(key,value){
if(this.supported){localStorage[key]=value}
else{$raise('NameError',"local storage is not supported by this browser")}
}
}
local_storage=new $LocalStorageClass()
