<?php
	$request = array("type" => $_GET['type'],
					 "s_date" => intval($_GET['s_date']),
					 "e_date" => intval($_GET['e_date']),
					 "location" => $_GET['location']);
					 
	require('arrays.php');
	
	// Functions
	
	function bad_params($param)
	{
		echo "Bad " . $param . " parameter. <a href=\"stats.html\">Go back</a>.";
	};
	
	// Request Handler
	/*				 
	if($request['type'] != "Literacy" && $request['type'] != "HashFreq" && $request['type'] != "WordFreq")
		bad_params("type");
		
	else if($request['s_date'] != 2 && $request['s_date'] != 3 && $request['s_date'] != 4)
		bad_params("start date");
	
	else if($request['e_date'] != 2 && $request['e_date'] != 3 && $request['e_date'] != 4)
		bad_params("end date");
		
	else if($request['e_date'] < $request['s_date'])
		bad_params("date range");
		
	else if(!in_array($request['location'], $state_names))
		bad_params("location");*/
	if(false) {echo "lolwut";}
	else
	{
		// Do all the good shit here
	?>
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Twitter EmotiMap</title>
    
    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
    <link rel="shortcut icon" href="favicon.ico" />
    <script src="http://code.jquery.com/jquery.js"></script>
    <script src="js/bootstrap.min.js"></script>
    
    <style type="text/css">
	.map_render{
		width: 100%;	
	}
	
	
	/* Table */
	#data-table {
		border: none; /* Turn off all borders */
		border-top: 1px solid #ccc;
		width: 540px;
	}
	#data-table caption {
		color: #545454;
		font-size: 14px;
		font-weight: normal;
		line-height: 20px;
		margin: 0 0 20px 0;
		padding: 0;
		text-align: center;
	}
	#data-table thead {
		background: #f0f0f0;
	}
	#data-table th, 
	#data-table td {
		border: none; /* Turn off all borders */
		border-bottom: 1px solid #ccc;
		margin: 0;
		padding: 10px;
		text-align: left;	
	}
	
	/* Toggle */
	.toggles {
		background: #ebebeb;	
		color: #545454;
		height: 20px;
		padding: 15px;
	}
	.toggles p {
		margin: 0;
	}
	.toggles a {
		background: #222;
		border-radius: 3px;	
		color: #fff;
		display: block;
		float: left;
		margin: 0 10px 0 0;
		padding: 0 6px;
		text-decoration: none;
	}
	.toggles a:hover {
		background: #666;
	}
	#reset-graph-button {
		float:right;
	}
	
	/* Graph */
	/* Containers */
	#wrapper {
		height: 420px;
		left: 50%;
		margin: -210px 0 0 -270px;
		position: absolute;
		top: 50%;	
		width: 540px;
	}
	#figure {
		height: 380px;
		position: relative;
	}
	#figure ul {
		list-style: none;
		margin: 0;
		padding: 0;
	}
	.graph {
		height: 283px;
		position: relative;
	}
	
	/* Legend */
	.legend {
		background: #f0f0f0;
		border-radius: 4px;
		bottom: 0;
		position: absolute;
		text-align: left;
		width: 540px;	
	}
	.legend li {
		display: block;
		float: left;
		height: 20px;
		margin: 0;
		padding: 10px 30px;
		width: 120px;
	}
	.legend span.icon {
		background-position: 50% 0;
		border-radius: 2px;
		display: block;
		float: left;
		height: 16px;
		margin: 2px 10px 0 0;
		width: 16px;	
	}
	
	/* X-Axis */
	.x-axis {
		bottom: 0;
		color: #555;
		position: absolute;
		text-align: center;
		width: 540px;
	}
	.x-axis li {
		float: left;
		margin: 0 15px;
		padding: 5px 0;
		width: 76px;	
	}
	
	/* Y-Axis */
	.y-axis {
		color: #555;
		position: absolute;
		text-align: right;
		width: 100%;
	}
	.y-axis li {
		border-top: 1px solid #ccc;
		display: block;
		height: 62px;
		width: 100%;
	}
	.y-axis li span {
		display: block;
		margin: -10px 0 0 -60px;
		padding: 0 10px;
		width: 40px;
	}
	
	/* Graph Bars */
	.bars {
		height: 253px;
		position: absolute;
		width: 100%;
		z-index: 10;
	}
	.bar-group {
		float: left;
		height: 100%;
		margin: 0 15px;
		position: relative;
		width: 76px;
	}
	.bar {
		border-radius: 3px 3px 0 0;
		bottom: 0;
		cursor: pointer;	
		height: 0;
		position: absolute;
		text-align: center;
		width: 24px;
	}
	.bar.fig0 {
		left: 0;
	}
	.bar.fig1 {
		left: 26px;
	}
	.bar.fig2 {
		left: 52px;
	}
	.bar span {
		background: #fefefe;
		border-radius: 3px;
		left: -8px;
		display: none;
		margin: 0;
		position: relative;
		text-shadow: rgba(255, 255, 255, 0.8) 0 1px 0;
		width: 40px;
		z-index: 20;
		
		-webkit-box-shadow: rgba(0, 0, 0, 0.6) 0 1px 4px;
		box-shadow: rgba(0, 0, 0, 0.6) 0 1px 4px;
	}
	.bar:hover span {
		display: block;
		margin-top: -25px;
	}
	
	#data-table {
		display: none;
	}
	.bar span {
	   background: -webkit-gradient(linear, left top, left bottom, color-stop(0.0, #fff), color-stop(1.0, #e5e5e5));
	   display: block;
	   opacity: 0;
	
	   -webkit-transition: all 0.2s ease-out;
	}
	
	.bar:hover span {
	   opacity: 1;
	}
	.fig0 {
	   background: -webkit-gradient(linear, left top, right top, color-stop(0.0, #747474), color-stop(0.49, #676767), color-stop(0.5, #505050), color-stop(1.0, #414141));
	}
	
	.fig1 {
	   background: -webkit-gradient(linear, left top, right top, color-stop(0.0, #65c2e8), color-stop(0.49, #55b3e1), color-stop(0.5, #3ba6dc), color-stop(1.0, #2794d4));
	}
	
	.fig2 {
	   background: -webkit-gradient(linear, left top, right top, color-stop(0.0, #eea151), color-stop(0.49, #ea8f44), color-stop(0.5, #e67e28), color-stop(1.0, #e06818));
	}
	</style>
    
    <script type="text/javascript">
	/**
	 *	Animated Graph Tutorial for Smashing Magazine
	 *	July 2011
	 *   
	 * 	Author:	Derek Mack
	 *			derekmack.com
	 *			@derek_mack
	 *
	 *	Example 3 - Animated Bar Chart via jQuery
	 */
	
	// Wait for the DOM to load everything, just to be safe
	$(document).ready(function() {
	
		// Create our graph from the data table and specify a container to put the graph in
		createGraph('#data-table', '.chart');
		
		// Here be graphs
		function createGraph(data, container) {
			// Declare some common variables and container elements	
			var bars = [];
			var figureContainer = $('<div id="figure"></div>');
			var graphContainer = $('<div class="graph"></div>');
			var barContainer = $('<div class="bars"></div>');
			var data = $(data);
			var container = $(container);
			var chartData;		
			var chartYMax;
			var columnGroups;
			
			// Timer variables
			var barTimer;
			var graphTimer;
			
			// Create table data object
			var tableData = {
				// Get numerical data from table cells
				chartData: function() {
					var chartData = [];
					data.find('tbody td').each(function() {
						chartData.push($(this).text());
					});
					return chartData;
				},
				// Get heading data from table caption
				chartHeading: function() {
					var chartHeading = data.find('caption').text();
					return chartHeading;
				},
				// Get legend data from table body
				chartLegend: function() {
					var chartLegend = [];
					// Find th elements in table body - that will tell us what items go in the main legend
					data.find('tbody th').each(function() {
						chartLegend.push($(this).text());
					});
					return chartLegend;
				},
				// Get highest value for y-axis scale
				chartYMax: function() {
					var chartData = this.chartData();
					// Round off the value
					var chartYMax = Math.ceil(Math.max.apply(Math, chartData) / 1000) * 1000;
					return chartYMax;
				},
				// Get y-axis data from table cells
				yLegend: function() {
					var chartYMax = this.chartYMax();
					var yLegend = [];
					// Number of divisions on the y-axis
					var yAxisMarkings = 5;						
					// Add required number of y-axis markings in order from 0 - max
					for (var i = 0; i < yAxisMarkings; i++) {
						yLegend.unshift(((chartYMax * i) / (yAxisMarkings - 1)) / 1000);
					}
					return yLegend;
				},
				// Get x-axis data from table header
				xLegend: function() {
					var xLegend = [];
					// Find th elements in table header - that will tell us what items go in the x-axis legend
					data.find('thead th').each(function() {
						xLegend.push($(this).text());
					});
					return xLegend;
				},
				// Sort data into groups based on number of columns
				columnGroups: function() {
					var columnGroups = [];
					// Get number of columns from first row of table body
					var columns = data.find('tbody tr:eq(0) td').length;
					for (var i = 0; i < columns; i++) {
						columnGroups[i] = [];
						data.find('tbody tr').each(function() {
							columnGroups[i].push($(this).find('td').eq(i).text());
						});
					}
					return columnGroups;
				}
			}
			
			// Useful variables for accessing table data		
			chartData = tableData.chartData();		
			chartYMax = tableData.chartYMax();
			columnGroups = tableData.columnGroups();
			
			// Construct the graph
			
			// Loop through column groups, adding bars as we go
			$.each(columnGroups, function(i) {
				// Create bar group container
				var barGroup = $('<div class="bar-group"></div>');
				// Add bars inside each column
				for (var j = 0, k = columnGroups[i].length; j < k; j++) {
					// Create bar object to store properties (label, height, code etc.) and add it to array
					// Set the height later in displayGraph() to allow for left-to-right sequential display
					var barObj = {};
					barObj.label = this[j];
					barObj.height = Math.floor(barObj.label / chartYMax * 100) + '%';
					barObj.bar = $('<div class="bar fig' + j + '"><span>' + barObj.label + '</span></div>')
						.appendTo(barGroup);
					bars.push(barObj);
				}
				// Add bar groups to graph
				barGroup.appendTo(barContainer);			
			});
			
			// Add heading to graph
			var chartHeading = tableData.chartHeading();
			var heading = $('<h4>' + chartHeading + '</h4>');
			heading.appendTo(figureContainer);
			
			// Add legend to graph
			var chartLegend	= tableData.chartLegend();
			var legendList	= $('<ul class="legend"></ul>');
			$.each(chartLegend, function(i) {			
				var listItem = $('<li><span class="icon fig' + i + '"></span>' + this + '</li>')
					.appendTo(legendList);
			});
			legendList.appendTo(figureContainer);
			
			// Add x-axis to graph
			var xLegend	= tableData.xLegend();		
			var xAxisList	= $('<ul class="x-axis"></ul>');
			$.each(xLegend, function(i) {			
				var listItem = $('<li><span>' + this + '</span></li>')
					.appendTo(xAxisList);
			});
			xAxisList.appendTo(graphContainer);
			
			// Add y-axis to graph	
			var yLegend	= tableData.yLegend();
			var yAxisList	= $('<ul class="y-axis"></ul>');
			$.each(yLegend, function(i) {			
				var listItem = $('<li><span>' + this + '</span></li>')
					.appendTo(yAxisList);
			});
			yAxisList.appendTo(graphContainer);		
			
			// Add bars to graph
			barContainer.appendTo(graphContainer);		
			
			// Add graph to graph container		
			graphContainer.appendTo(figureContainer);
			
			// Add graph container to main container
			figureContainer.appendTo(container);
			
			// Set individual height of bars
			function displayGraph(bars, i) {
			   // Changed the way we loop because of issues with $.each not resetting properly
			   if (i < bars.length) {
				  // Add transition properties and set height via CSS
				  $(bars[i].bar).css({'height': bars[i].height, '-webkit-transition': 'all 0.8s ease-out'});
				  // Wait the specified time, then run the displayGraph() function again for the next bar
				  barTimer = setTimeout(function() {
					 i++;
					 displayGraph(bars, i);
				  }, 100);
			   }
			}
			// Reset graph settings and prepare for display
			function resetGraph() {
			   // Set bar height to 0 and clear all transitions
			   $.each(bars, function(i) {
				  $(bars[i].bar).stop().css({'height': 0, '-webkit-transition': 'none'});
			   });
			
			   // Clear timers
			   clearTimeout(barTimer);
			   clearTimeout(graphTimer);
			
			   // Restart timer
			   graphTimer = setTimeout(function() {
				  displayGraph(bars, 0);
			   }, 200);
			}
			
			// Helper functions
			
			// Call resetGraph() when button is clicked to start graph over
			$('#reset-graph-button').click(function() {
				resetGraph();
				return false;
			});
			
			// Finally, display graph via reset function
			resetGraph();
		}	
	});
	</script>
    
    </head>
    <body>
    <nav class="navbar navbar-default navbar-fixed-top" role="navigation">
      <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Twitter EmotiMap</a>
        </div>
    
        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav">
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About</a></li>
            <li class="active"><a href="stats.html">Map</a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">More <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="proposal.html">Project Text</a></li>
                <li class="divider"></li>
                <li><a href="matt.html">Matt Gross</a></li>
                <li><a href="max.html">Max Trotter</a></li>
                <li><a href="brian.html">Brian McWilliams</a></li>
                <li><a href="andrew.html">Andrew Mahan</a></li>
                <li><a href="dillon.html">Dillon Fancher</a></li>
              </ul>
            </li>
          </ul>
          <!--<form class="navbar-form navbar-left" role="search">
            <div class="form-group">
              <input type="text" class="form-control" placeholder="Search">
            </div>
            <button type="submit" class="btn btn-default">Submit</button>
          </form>
          <ul class="nav navbar-nav navbar-right">
            <li><a href="#">Link</a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="#">Action</a></li>
                <li><a href="#">Another action</a></li>
                <li><a href="#">Something else here</a></li>
                <li class="divider"></li>
                <li><a href="#">Separated link</a></li>
              </ul>
            </li>
          </ul>-->
        </div><!-- /.navbar-collapse -->
      </div><!-- /.container-fluid -->
    </nav>
    
    <div class="container-fluid" style="margin-top: 70px;">
        <form method="get" action="request.php#map">
        <div class="row">
            <!--<div class="col-md-offset-3 col-md-2">-->
	    <div class="col-md-offset-4 col-md-2">
                <select class="form-control" name="type">
                    <option selected value="<?php echo $request['type']; ?>"><?php echo $request['type']; ?></option>
                    <option value="Literacy">Literacy</option>
                    <!--<option value="Emotion">Emotion</option>-->
                    <option value="EmojiFreq">Emoji Frequency</option>
                    <option value="HashFreq">Hashtag Frequency</option>
                </select>
            </div>
	    <!--
            <div class="col-md-2">
                <select class="form-control" name="s_date">
                    <option selected value="<?php echo $request['s_date']; ?>"><?php echo $months[$request['s_date']]; ?></option>
                    <option value="2">February</option>
                    <option value="3">March</option>
                    <option value="4">April</option>
                </select><br />
                <select class="form-control" name="e_date">
                    <option selected value="<?php echo $request['e_date']; ?>"><?php echo $months[$request['e_date']]; ?></option>
                    <option value="2">February</option>
                    <option value="3">March</option>
                    <option value="4">April</option>
                </select>
            </div>
	    -->
            <div class="col-md-2">
                <select class="form-control" name="location">
                    <option selected value="<?php echo $request['location']; ?>"><?php echo $us_state_abbrevs_names[$request['location']]; ?></option>
                    <option value="ALL">U.S.A.</option>
                    <option value="DEN">Denver</option>
                    <option value="NYC">New York City</option>
                    <option value="NOR">New Orleans</option>
                    <option value="OAK">Oakland</option>
                    <option value="DET">Detroit</option>
                    <!--<option value="ALL">Entire U.S.</option>
                    <option value="AL">Alabama</option> 
                    <option value="AK">Alaska</option> 
                    <option value="AZ">Arizona</option> 
                    <option value="AR">Arkansas</option> 
                    <option value="CA">California</option> 
                    <option value="CO">Colorado</option> 
                    <option value="CT">Connecticut</option> 
                    <option value="DE">Delaware</option>
                    <option value="FL">Florida</option> 
                    <option value="GA">Georgia</option> 
                    <option value="HI">Hawaii</option> 
                    <option value="ID">Idaho</option> 
                    <option value="IL">Illinois</option> 
                    <option value="IN">Indiana</option> 
                    <option value="IA">Iowa</option> 
                    <option value="KS">Kansas</option> 
                    <option value="KY">Kentucky</option> 
                    <option value="LA">Louisiana</option> 
                    <option value="ME">Maine</option> 
                    <option value="MD">Maryland</option> 
                    <option value="MA">Massachusetts</option> 
                    <option value="MI">Michigan</option> 
                    <option value="MN">Minnesota</option> 
                    <option value="MS">Mississippi</option> 
                    <option value="MO">Missouri</option> 
                    <option value="MT">Montana</option> 
                    <option value="NE">Nebraska</option> 
                    <option value="NV">Nevada</option> 
                    <option value="NH">New Hampshire</option> 
                    <option value="NJ">New Jersey</option> 
                    <option value="NM">New Mexico</option> 
                    <option value="NY">New York</option> 
                    <option value="NC">North Carolina</option> 
                    <option value="ND">North Dakota</option> 
                    <option value="OH">Ohio</option> 
                    <option value="OK">Oklahoma</option> 
                    <option value="OR">Oregon</option> 
                    <option value="PA">Pennsylvania</option> 
                    <option value="RI">Rhode Island</option> 
                    <option value="SC">South Carolina</option> 
                    <option value="SD">South Dakota</option> 
                    <option value="TN">Tennessee</option> 
                    <option value="TX">Texas</option> 
                    <option value="UT">Utah</option> 
                    <option value="VT">Vermont</option> 
                    <option value="VA">Virginia</option> 
                    <option value="WA">Washington</option> 
                    <option value="WV">West Virginia</option> 
                    <option value="WI">Wisconsin</option> 
                    <option value="WY">Wyoming</option>-->
                </select>
            </div>
        </div>
        <br />
        <div class="row">
            <div class="col-md-offset-5 col-md-2" style="text-align: center;">
                <button type="submit" class="btn btn-success">Get Map</button>
            </div>
        </div>
        </form>
        
        
        <!-- MAP GOES HERE -->
        <div class="row">
        	<div class="col-md-offset-1 col-md-10">
                <div id="wrapper">
                 <div class="chart">
                    <h3>Population of endangered species from 2012 to 2016</h3>
                    <table id="data-table" border="1" cellpadding="10" cellspacing="0"
                    summary="The effects of the zombie outbreak on the populations
                    of endangered species from 2012 to 2016">
                       <caption>Population in thousands</caption>
                       <thead>
                          <tr>
                             <td>&nbsp;</td>
                             <th scope="col">2012</th>
                             <th scope="col">2013</th>
                             <th scope="col">2014</th>
                             <th scope="col">2015</th>
                             <th scope="col">2016</th>
                          </tr>
                       </thead>
                       <tbody>
                          <tr>
                             <th scope="row">Carbon Tiger</th>
                             <td>4080</td>
                             <td>6080</td>
                             <td>6240</td>
                             <td>3520</td>
                             <td>2240</td>
                          </tr>
                          <tr>
                             <th scope="row">Blue Monkey</th>
                             <td>5680</td>
                             <td>6880</td>
                             <td>6240</td>
                             <td>5120</td>
                             <td>2640</td>
                          </tr>
                          <tr>
                             <th scope="row">Tanned Zombie</th>
                             <td>1040</td>
                             <td>1760</td>
                             <td>2880</td>
                             <td>4720</td>
                             <td>7520</td>
                          </tr>
                       </tbody>
                    </table>
                 </div>
              </div>
            </div>
        </div>
        
    </div>
    
    </body>
    </html>
    <?php
	}
?>
