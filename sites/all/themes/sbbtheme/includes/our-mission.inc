<h1 class="real-page-title page-header">Our mission</h1>

<div class="row">
  <div class="col-md-3 hidden-xs hidden-sm scrollspy-target">

    <ul class="nav nav-list sbb-sidenav" data-spy="affix" data-offset-top="286" data-offset-bottom="270">
      <li class="active"><a href="#cubesats" class="nav-link"><i></i> <span>Cubesats</span></a></li>
      <li><a href="#improve" class="nav-link"><i></i> <span>Their value</span></a></li>
      <li><a href="#structure" class="nav-link"><i></i> <span>Their structure</span></a></li>
      <li><a href="#fund" class="nav-link"><i></i> <span>What we will fund</span></a></li>
      <li><a href="#no-space-debris" class="nav-link"><i></i> <span>No space debris</span></a></li>
      <li>
        <?php include_once(drupal_get_path('theme', 'sbbtheme') . '/featured-sponsor/featured-sponsor.inc.php'); sbb_generate_featured_sponsor(); ?>
      </li>
    </ul>

  </div>
  <div class="col-md-9 content">

    <?php if(! sbb_on_mobile()): ?>
    <p class="mission" style="margin-top:30px; margin-bottom:100px;">Our mission is to <span class="larger">support space research</span> by launching the <span class="larger">first billboard into space</span> ever.</p>
    <div class="promo">
      <iframe src="//player.vimeo.com/video/80134768?title=0&amp;byline=0&amp;portrait=0&amp;autoplay=0" width="694" height="390" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
    </div>
    <?php else: ?>
    <img src="<?php sbb_echo_theme_file('resources/img/our-mission/cubesat.jpg'); ?>" class="img-responsive"/>
    <p class="mission" style="">Our mission is to <span class="larger">support space research</span> by launching the <span class="larger">first billboard into space</span> ever.</p>
    <?php endif; ?>

    <section id="cubesats">
      <h2 class="page-header">CubeSats</h2>

      <p class="description">SpaceBillboard supports <span class="accent">innovative space research</span>. More precisely, we want to support research on <span class="accent">CubeSats</span>. The first CubeSats were developed as student projects in universities, but by now, space agencies such as <span class="accent">NASA and ESA</span> have recognized their potential. But what makes them so special?</p>

      <div class="row info">
        <div class="col-md-6 text">
          <h1>Smaller is better</h1>
          <p class="explanation-text">CubeSats are small satellites that could fit <span class="accent">in the palm of your hand</span> while traditional satellites are the size of a washing machine or even a mini-van. Because of this, CubeSats <span class="accent">weigh less</span> and <span class="accent">consume less power</span>. Moreover, CubeSats can be launched together with a larger satellite, making them also <span class="accent">cheaper to launch</span>.</p>
        </div>
        <div class="col-md-6 icons">
          <div class="row">
            <div class="col-xs-4">
              <div class="explanation">
                Small size
              </div>
            </div>
            <div class="col-xs-4">
              <div class="explanation">
                Low weight
              </div>
            </div>
            <div class="col-xs-4">
              <div class="explanation">
                Low power
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-4">
              <div class="img" style="background-image: url(<?php sbb_echo_theme_file('resources/img/our-mission/milk-carton.png'); ?>);"></div>
            </div>
            <div class="col-xs-4">
              <div class="img" style="background-image: url(<?php sbb_echo_theme_file('resources/img/our-mission/feather.png'); ?>); background-size: 100% auto;"></div>
            </div>
            <div class="col-xs-4">
              <div class="img" style="background-image: url(<?php sbb_echo_theme_file('resources/img/our-mission/power.png'); ?>);"></div>
            </div>
          </div>        
        </div>
      </div> <!-- </info> -->

      <div class="row info">
        <div class="col-md-6 text">
          <h1>Small, but powerful</h1>
          <p class="explanation-text">While CubeSats may be small, they can definitely outperform a large satellite! The real power of CubeSats is revealed when they <span class="accent">work together</span>. By launching a constellation of CubeSats, we can assure that every area on Earth is at all times covered by a satellite, something which is impossible with one large satellite. And while a <span class="accent">malfunction</span> in the large satellite means the end of the mission, a problem with one of the CubeSats is <span class="accent">far less disastrous</span>.</p>
        </div>
        <div class="col-md-6 icons">
          <div class="row">
          </div>
          <div class="row">
            <div class="col-xs-12">
              <div class="img" style="background-image: url(<?php sbb_echo_theme_file('resources/img/our-mission/network.png'); ?>);"></div>
            </div>
          </div>        
        </div>
      </div> <!-- </info> -->

      <div class="row info">
        <div class="col-md-6 text">
          <h1>Off-the-shelf components</h1>
          <p class="explanation-text"><span class="accent">Traditionally</span>, space designers prefer to use components that have already proven to work in space because you cannot replace a broken component once the satellite is in orbit. Because of this attitude, the advancement of satellite technology progresses slowly. <span class="accent">CubeSats represent a different design philosophy:</span> Because CubeSats cost far less than a traditional satellite, CubeSat designers use as many commercially available components as possible, like the components in your smart phone. These components are <span class="accent">cheaper </span> and usually far <span class="accent">more powerful </span> than components in most existing satellites.</p>
        </div>
        <div class="col-md-6 icons">
          <div class="row">
          </div>
          <div class="row">
            <div class="col-xs-12">
              <div class="img smartphone" style="background-image: url(<?php sbb_echo_theme_file('resources/img/our-mission/smartphone.png'); ?>); height: 250px;"></div>
            </div>
          </div>        
        </div>
      </div> <!-- </info> -->

      <div class="row info">
        <div class="col-md-6 text">
          <h1>Space research 2.0</h1>
          <p class="explanation-text">As a result of all this, CubeSats can be <span class="accent">developed faster and cheaper</span>. As such, CubeSats <span class="accent">make space research accessible for universities all around the world</span> and put space research in higher gear, leading to <span class="accent">amazing possibilities</span>!</p>
        </div>
        <div class="col-md-6 icons">
          <div class="row">
            <div class="col-xs-12">
              <div class="img" style="background-image: url(<?php sbb_echo_theme_file('resources/img/our-mission/amazing-possibilities.png'); ?>);"></div>
            </div>
          </div>        
        </div>
      </div> <!-- </info> -->
    </section>

    <div class="visible-xs visible-sm">
      <?php sbb_generate_horizontal_featured_sponsor(); ?>
    </div>
      
    <section id="improve">
      <h2 class="page-header">How CubeSats can improve our lives</h2>

      <p class="description">So the possibilities of CubeSats for advancing space research are vast. And that space research can also <span class="accent">improve our lives</span> here on Earth! Here are <span class="accent">some examples</span> of what CubeSats can do.</p>

      <div class="row info">
        <div class="col-md-4">
          <div class="img" style="background-image: url(<?php sbb_echo_theme_file('resources/img/our-mission/radio.png'); ?>);"></div>
        </div>
        <div class="col-md-8 text">
          <h1>Data transmission</h1>
          <p class="explanation-text">The <span class="accent">internet </span> has in no time become a big part of our lives. So much so, that life seems to come to a halt when no connection can be made.</p>
          <p class="explanation-text">With CubeSats, a constellation can be formed that can <span class="accent">give internet accessibility to everyone on Earth</span>, for a low cost. This way, travelers will be able to check interesting locations on the internet so that they can get the most out of their journey, farmers living in remote areas will be able to order products on-line and you will be connected to the world at all time.</p>
        </div>
      </div> <!-- </info> -->

      <div class="row info">
        <div class="col-md-4">
          <div class="row">
            <div class="col-md-12">
              <div class="img" style="background-image: url(<?php sbb_echo_theme_file('resources/img/our-mission/trash-can.png'); ?>);"></div>
            </div>
          </div>        
        </div>
        <div class="col-md-8 text">
          <h1>Debris mitigation</h1>
          <p class="explanation-text">The list of inactive satellites and man-made objects orbiting the Earth is ever increasing. This <span class="accent">space debris poses a serious threat</span> to active satellites, and worse, to astronauts.</p>
          <p class="explanation-text"><span class="accent">CubeSats do not contribute to space debris</span> because they are launched in low orbits and make their re-entry after a maximum of 25 years in orbit. In addition, research is currently going on to <span class="accent">develop CubeSats that could remove space debris</span> using claws, nets, magnets...</p>
        </div>
      </div> <!-- </info> -->

      <div class="row info">
        <div class="col-md-4">
          <div class="row">
            <div class="col-md-12">
              <div class="img" style="background-image: url(<?php sbb_echo_theme_file('resources/img/our-mission/telescope.png'); ?>);"></div>
            </div>
          </div>        
        </div>
        <div class="col-md-8 text">
          <h1>Science and exploration</h1>
          <p class="explanation-text">There is a whole lot to discover and explore in space and <span class="accent">CubeSats are perfect to help us with this exploration</span>. For some fields of research, CubeSats are even <span class="accent">the only acceptable type of satellite</span> to do the trick. For example, spacecraft run the highest risk during re-entry at altitudes below 300 km, so we should definitely understand this part of space well. Because the satellites that perform this research also make their re-entry and burn up in a short time, it only makes sense economically to use cheap satellites such as CubeSats for this.</p>
        </div>
      </div> <!-- </info> -->

      <div class="row info">
        <div class="col-md-4">
          <div class="row">
            <div class="col-md-12">
              <div class="img" style="background-image: url(<?php sbb_echo_theme_file('resources/img/our-mission/observation.png'); ?>);"></div>
            </div>
          </div>        
        </div>
        <div class="col-md-8 text">
          <h1>Earth observation</h1>
          <p class="explanation-text">Orbiting way up above, satellites have a nice view on our Earth. From the very beginning of space research, satellites have given <span class="accent">farmers</span> crucial data about their crops and have saved numerous lives by <span class="accent">predicting natural disasters</span> such as hurricanes and forest fires. And when a disaster has struck, satellite imagery is analysed to make sure that help is sent where it is needed the most.</p>
          <p class="explanation-text">CubeSats can easily <span class="accent">perform Earth observation for a fraction of the cost of current satellites</span>. When used in numbers, they can assure that every area on Earth is covered, yielding valuable data for everyone on Earth.</p>
        </div>
      </div> <!-- </info> -->

      <div class="row info">
        <div class="col-md-4">
          <div class="row">
            <div class="col-md-12">
              <div class="img" style="background-image: url(<?php sbb_echo_theme_file('resources/img/our-mission/education.png'); ?>);"></div>
            </div>
          </div>        
        </div>
        <div class="col-md-8 text">
          <h1>Educate and inspire</h1>
          <p class="explanation-text"><span class="accent">We need passionate people</span> to create progress in this world! Last but not least, CubeSats are a great means to <a href="http://www.esa.int/Education/CubeSats">motivate</a> students to work on scientific and technical problems. CubeSat projects <span class="accent">give students exciting hands-on experience with space projects</span> and allow them to work together in a team. The most important product of a CubeSat project is often not the satellite, but the team.</p>
        </div>
      </div> <!-- </info> -->

    </section>

    <section id="structure">
      <h2 class="page-header">Structure of a CubeSat</h2>

      <p class="description">In essence, a CubeSat consists of <span class="accent">several subsystems</span> which are put on top of each other on a “stack”. These systems all <span class="accent">work together</span> to make sure the payload can perform its task.</p>
      <div class="row info">
        <div class="col-md-7 col-sm-7">
          <p class="explanation-text"><strong><span class="accent">Payload</span></strong>: The payload is the reason the satellite is built, for example a camera or measurement instruments in a scientific satellite.</p>
          <p class="explanation-text"><strong><span class="accent">ADCS</span></strong>: The Attitude Determination and Control System orientates the CubeSat in space, for example to point a camera to Earth.</p>
          <p class="explanation-text"><strong><span class="accent">OBC</span></strong>: The On-Board Computer is the brain of the satellite. It forwards information between the different subsystems and makes sure that they perform their tasks.</p>
          <p class="explanation-text"><strong><span class="accent">Comm</span></strong>: The communication system controls the communication with the mission controllers on Earth or with other CubeSats in space.</p>
          <p class="explanation-text"><strong><span class="accent">EPS</span></strong>: The Electric Power System contains the batteries that power the CubeSat.</p>
          <p class="explanation-text"><strong><span class="accent">Solar Panels</span></strong>: The solar panels recharge the batteries in the EPS.</p>
          <p class="explanation-text"><strong><span class="accent">Antenna</span></strong>: The antenna actually transmits the communication with the mission controllers and with other CubeSats.</p>
        </div>
        <div class="col-md-5 col-sm-5">
          <img src="<?php sbb_echo_theme_file('resources/img/our-mission/render.png'); ?>" class="img-responsive center-block" />
        </div>
      </div>
    </section>


      
    <section id="fund">
      <h2 class="page-header">What we will fund</h2>

      <p class="description">So CubeSats can clearly play a very important role in the future of space research and with SpaceBillboard, we want to <span class="accent">give CubeSats and space research an extra boost</span>. Our wish list of things we want to do is quite long, but these are the most important ones:</p>

      <div class="row info">
        <div class="col-md-4">
          <div class="row">
            <div class="col-md-12">
              <div class="img" style="background-image: url(<?php sbb_echo_theme_file('resources/img/our-mission/team.png'); ?>);"></div>
            </div>
          </div>        
        </div>
        <div class="col-md-8 text">
          <h1>Support student projects</h1>
          <p class="explanation-text">CubeSats are great satellites to give students hands-on experience with satellite development. They contain all the important systems that are required in a satellite and because of their small size and low cost, university students can work on them too. Not only do these students learn a great deal this way, they also get inspired about space research! We will <span class="accent">fund student projects at KU Leuven</span> amongst others by constructing of test setups and buying necessary components such as an air bearing table to test our attitude determination and control system and 3D printing material to construct our star tracker baffle.</p>
        </div>
      </div> <!-- </info> -->

      <div class="row info">
        <div class="col-md-4">
          <div class="row">
            <div class="col-md-12">
              <div class="img" style="background-image: url(<?php sbb_echo_theme_file('resources/img/our-mission/rocket.png'); ?>);"></div>
            </div>
          </div>        
        </div>
        <div class="col-md-8 text">
          <h1>Fund a future launch</h1>
          <p class="explanation-text">Once a satellite has been built, it still needs to get up in space. A rocket launch is quite expensive and acquiring a launch is often one of the big hurdles in a CubeSat project, but also the summum for space researchers and students. Therefore, we want to help <span class="accent">fund a future launch for a KU Leuven CubeSat</span>.</p>
        </div>
      </div> <!-- </info> -->

      <div class="row info">
        <div class="col-md-4">
          <div class="row">
            <div class="col-md-12">
              <div class="img" style="background-image: url(<?php sbb_echo_theme_file('resources/img/our-mission/radio.png'); ?>);"></div>
            </div>
          </div>        
        </div>
        <div class="col-md-8 text">
          <h1>Build a ground station</h1>
          <p class="explanation-text">And once a CubeSat has been launched, we have to get their results back on the ground. To get those results, and to send commands up to the satellite, we need a ground station. Therefore, we plan to <span class="accent">fund the construction of a ground station</span>. The good thing is, other CubeSats and satellites will be able to use it too! The more ground stations a satellite can use, the more frequently the operators on Earth can download data and the more useful the CubeSat becomes!</p>
        </div>
      </div> <!-- </info> -->

      <div class="row info">
        <div class="col-md-4">
          <div class="row">
            <div class="col-md-12">
              <div class="img" style="background-image: url(<?php sbb_echo_theme_file('resources/img/our-mission/future-research.png'); ?>);"></div>
            </div>
          </div>        
        </div>
        <div class="col-md-8 text">
          <h1>Start new research</h1>
          <p class="explanation-text">We are only at the beginning of finding out what CubeSats can give us and we want to make sure that this research can enter new levels. We want to <span class="accent">start up new and groundbreaking research</span> at KU Leuven, such as formation flying with CubeSats, autonomous docking (two satellites connecting in space), high accuracy pointing platforms to make even more accurate measurements, etc.</p>
        </div>
      </div> <!-- </info> -->

    </section>

    
    <section id="no-space-debris">
      <h2 class="page-header">No space debris</h2>

      <p class="description">Because we are fond of space, it is very important to us that <span class="accent">SpaceBillboard does not add to any useless space debris</span>. Therefore, the billboard will be launched into space on board of a satellite that performs a valuable mission as its primary goal and we make sure that the billboard does not hinder this satellite.</p>
      
    </section>

  </div>
</div>
