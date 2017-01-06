<?php if ( ! defined("BASEPATH")) exit("No direct script access allowed");

class Lp_sqlserver extends Front_Controller {

    function __construct(){
		parent::__construct();
        $this->load->model('servers_sqlserver_model','server');
        $this->load->model("option_model","option");
		$this->load->model("sqlserver_model","sqlserver");
        $this->load->model("os_model","os");  
	}

        public function index2(){

        $sqlserver_statistics = array();
        $sqlserver_statistics["sqlserver_servers_up"] = $this->db->query("select count(*) as num from sqlserver_status where connect=1")->row()->num;
        $sqlserver_statistics["sqlserver_servers_down"] = $this->db->query("select count(*) as num from sqlserver_status  where connect!=1")->row()->num;
        $data["sqlserver_statistics"] = $sqlserver_statistics;
        //print_r($mysql_statistics);
        $data["sqlserver_versions"] = $this->db->query("select sqlserver_version as versions, count(*) as num from sqlserver_status where sqlserver_version !='0' GROUP BY versions")->result_array();
        
        $data['sqlserver_connected_clients_ranking'] = $this->db->query("select server.host,server.port,status.connected_clients
        value from sqlserver_status status left join db_servers_sqlserver server
on `status`.server_id=`server`.id order by connected_clients desc limit 10;")->result_array();
        $data['sqlserver_used_memory_ranking'] = $this->db->query("select server.host,server.port,status.used_memory
        value from sqlserver_status status left join db_servers_sqlserver server
on `status`.server_id=`server`.id order by used_memory desc limit 10;")->result_array();
       
        $this->layout->view("sqlserver/index",$data);
    }

    
    public function index()
	{
        parent::check_privilege();
        $data["datalist"]=$this->sqlserver->get_status_total_record();

        $setval["host"]=isset($_GET["host"]) ? $_GET["host"] : "";
        $setval["tags"]=isset($_GET["tags"]) ? $_GET["tags"] : "";
        
        $setval["order"]=isset($_GET["order"]) ? $_GET["order"] : "";
        $setval["order_type"]=isset($_GET["order_type"]) ? $_GET["order_type"] : "";
        $data["setval"]=$setval;
  
        $this->layout->view("sqlserver/index",$data);
    }


    
    public function chart()
    {
        parent::check_privilege('');
        $server_id = $this->uri->segment(3);
        $server_id=!empty($server_id) ? $server_id : "0";
        $begin_time = $this->uri->segment(4);
        $begin_time=!empty($begin_time) ? $begin_time : "30";
        $time_span = $this->uri->segment(5);
        $time_span=!empty($time_span) ? $time_span : "min";
        
        //图表
        $chart_reslut=array();              
        for($i=$begin_time;$i>=0;$i--){
            $timestamp=time()-60*$i;
            $time= date('YmdHi',$timestamp);
            $has_record = $this->sqlserver->check_has_record($server_id,$time);
            if($has_record){
                $chart_reslut[$i]['time']=date('Y-m-d H:i',$timestamp);
                $dbdata=$this->sqlserver->get_status_chart_record($server_id,$time);
                $chart_reslut[$i]['processes'] = $dbdata['processes'];
                $chart_reslut[$i]['processes_running'] = $dbdata['processes_running'];
                $chart_reslut[$i]['processes_waits'] = $dbdata['processes_waits'];
                $chart_reslut[$i]['connections_persecond'] = $dbdata['connections_persecond'];
                $chart_reslut[$i]['pack_received_persecond'] = $dbdata['pack_received_persecond'];
                $chart_reslut[$i]['pack_sent_persecond'] = $dbdata['pack_sent_persecond'];
                $chart_reslut[$i]['packet_errors_persecond'] = $dbdata['packet_errors_persecond'];
                

            }  
        }
        $data['chart_reslut']=$chart_reslut;
    
        $chart_option=array();
        if($time_span=='min'){
            $chart_option['formatString']='%H:%M';
        }
        else if($time_span=='hour'){
            $chart_option['formatString']='%H:%M';
        }
        else if($time_span=='day'){
            $chart_option['formatString']='%m/%d %H:%M';
        }
        
        $data['chart_option']=$chart_option;
      
        $data['begin_time']=$begin_time;
        $data['cur_server_id']=$server_id;
        $data["cur_server"] = $this->server->get_servers($server_id);
        $this->layout->view('sqlserver/chart',$data);
    }

   
   public function replication()
        {
        
        parent::check_privilege();
        $datalist=$this->sqlserver->get_replication_total_record();
        
        if(empty($_GET["search"])){
            $datalist = get_sqlserver_replication_tree($datalist);
        }
        

        $setval["role"]=isset($_GET["role"]) ? $_GET["role"] : "";
        $setval["order"]=isset($_GET["order"]) ? $_GET["order"] : "";
        $setval["order_type"]=isset($_GET["order_type"]) ? $_GET["order_type"] : "";
        $data["setval"]=$setval;
        
        
        $data['datalist']=$datalist;

        $this->layout->view("sqlserver/replication",$data);
        }
    
}

/* End of file sqlserver.php */
/* Location: ./application/controllers/sqlserver.php */
