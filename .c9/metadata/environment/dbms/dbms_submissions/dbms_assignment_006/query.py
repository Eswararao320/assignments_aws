{"filter":false,"title":"query.py","tooltip":"/dbms/dbms_submissions/dbms_assignment_006/query.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":1,"column":199},"end":{"row":1,"column":200},"action":"insert","lines":["'"],"id":195}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":97},"action":"insert","lines":["Get all the distinct actors ids who acted in all movie whose title starts with Young Latin Girls."],"id":196}],[{"start":{"row":4,"column":74},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":197}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["Q"],"id":198},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["3"]}],[{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":[" "],"id":199}],[{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"remove","lines":[" "],"id":200}],[{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["="],"id":201}],[{"start":{"row":2,"column":3},"end":{"row":2,"column":5},"action":"insert","lines":["''"],"id":202}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["'"],"id":203}],[{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["S"],"id":204},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["E"]}],[{"start":{"row":2,"column":6},"end":{"row":2,"column":8},"action":"remove","lines":["SE"],"id":205},{"start":{"row":2,"column":6},"end":{"row":2,"column":12},"action":"insert","lines":["SELECT"]}],[{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":[" "],"id":206}],[{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"remove","lines":[" "],"id":207},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"remove","lines":["T"]},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"remove","lines":["C"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"remove","lines":["E"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"remove","lines":["L"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"remove","lines":["E"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"remove","lines":["S"]}],[{"start":{"row":2,"column":6},"end":{"row":2,"column":150},"action":"insert","lines":["SELECT fname,lname FROM (Actor INNER JOIN Cast on `Cast`.pid = `Actor`.id) INNER JOIN Movie on `Movie`.id = `Cast`.mid WHERE `Movie`.id = 12148;"],"id":208}],[{"start":{"row":2,"column":150},"end":{"row":2,"column":151},"action":"insert","lines":["'"],"id":209},{"start":{"row":2,"column":151},"end":{"row":2,"column":152},"action":"insert","lines":["'"]},{"start":{"row":2,"column":152},"end":{"row":2,"column":153},"action":"insert","lines":["'"]}],[{"start":{"row":2,"column":148},"end":{"row":2,"column":149},"action":"remove","lines":["8"],"id":210},{"start":{"row":2,"column":147},"end":{"row":2,"column":148},"action":"remove","lines":["4"]},{"start":{"row":2,"column":146},"end":{"row":2,"column":147},"action":"remove","lines":["1"]},{"start":{"row":2,"column":145},"end":{"row":2,"column":146},"action":"remove","lines":["2"]},{"start":{"row":2,"column":144},"end":{"row":2,"column":145},"action":"remove","lines":["1"]},{"start":{"row":2,"column":143},"end":{"row":2,"column":144},"action":"remove","lines":[" "]},{"start":{"row":2,"column":142},"end":{"row":2,"column":143},"action":"remove","lines":["="]},{"start":{"row":2,"column":141},"end":{"row":2,"column":142},"action":"remove","lines":[" "]},{"start":{"row":2,"column":140},"end":{"row":2,"column":141},"action":"remove","lines":["d"]},{"start":{"row":2,"column":139},"end":{"row":2,"column":140},"action":"remove","lines":["i"]},{"start":{"row":2,"column":138},"end":{"row":2,"column":139},"action":"remove","lines":["."]}],[{"start":{"row":2,"column":137},"end":{"row":2,"column":138},"action":"remove","lines":["`"],"id":211},{"start":{"row":2,"column":136},"end":{"row":2,"column":137},"action":"remove","lines":["e"]},{"start":{"row":2,"column":135},"end":{"row":2,"column":136},"action":"remove","lines":["i"]},{"start":{"row":2,"column":134},"end":{"row":2,"column":135},"action":"remove","lines":["v"]},{"start":{"row":2,"column":133},"end":{"row":2,"column":134},"action":"remove","lines":["o"]},{"start":{"row":2,"column":132},"end":{"row":2,"column":133},"action":"remove","lines":["M"]}],[{"start":{"row":2,"column":131},"end":{"row":2,"column":132},"action":"remove","lines":["`"],"id":212}],[{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"remove","lines":["e"],"id":213},{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"remove","lines":["m"]},{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"remove","lines":["a"]},{"start":{"row":2,"column":20},"end":{"row":2,"column":21},"action":"remove","lines":["n"]},{"start":{"row":2,"column":19},"end":{"row":2,"column":20},"action":"remove","lines":["l"]},{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"remove","lines":[","]},{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"remove","lines":["e"]},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"remove","lines":["m"]},{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"remove","lines":["a"]},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"remove","lines":["n"]},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"remove","lines":["f"]}],[{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["D"],"id":214},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["I"]}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["S"],"id":215},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["T"]}],[{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"remove","lines":["T"],"id":216},{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"remove","lines":["S"]}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["C"],"id":217}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"remove","lines":["C"],"id":218}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["C"],"id":219}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"remove","lines":["C"],"id":220}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["S"],"id":221},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["T"]}],[{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"insert","lines":["I"],"id":222},{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"insert","lines":["N"]},{"start":{"row":2,"column":19},"end":{"row":2,"column":20},"action":"insert","lines":["C"]}],[{"start":{"row":2,"column":20},"end":{"row":2,"column":21},"action":"insert","lines":["T"],"id":223}],[{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"insert","lines":[" "],"id":224}],[{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"remove","lines":[" "],"id":225}],[{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"insert","lines":["("],"id":226},{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"insert","lines":["A"]}],[{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"insert","lines":["c"],"id":227},{"start":{"row":2,"column":24},"end":{"row":2,"column":25},"action":"insert","lines":["t"]},{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"insert","lines":["o"]}],[{"start":{"row":2,"column":26},"end":{"row":2,"column":27},"action":"insert","lines":["."],"id":228},{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"insert","lines":["i"]}],[{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"insert","lines":["d"],"id":229},{"start":{"row":2,"column":29},"end":{"row":2,"column":30},"action":"insert","lines":[")"]}],[{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"insert","lines":["`"],"id":230}],[{"start":{"row":2,"column":30},"end":{"row":2,"column":31},"action":"insert","lines":["`"],"id":231}],[{"start":{"row":2,"column":139},"end":{"row":2,"column":140},"action":"insert","lines":["`"],"id":232},{"start":{"row":2,"column":140},"end":{"row":2,"column":141},"action":"insert","lines":["M"]},{"start":{"row":2,"column":141},"end":{"row":2,"column":142},"action":"insert","lines":["o"]}],[{"start":{"row":2,"column":142},"end":{"row":2,"column":143},"action":"insert","lines":["v"],"id":233}],[{"start":{"row":2,"column":140},"end":{"row":2,"column":143},"action":"remove","lines":["Mov"],"id":234},{"start":{"row":2,"column":140},"end":{"row":2,"column":145},"action":"insert","lines":["Movie"]}],[{"start":{"row":2,"column":145},"end":{"row":2,"column":146},"action":"insert","lines":["`"],"id":235},{"start":{"row":2,"column":146},"end":{"row":2,"column":147},"action":"insert","lines":["."]}],[{"start":{"row":2,"column":147},"end":{"row":2,"column":148},"action":"insert","lines":["n"],"id":236},{"start":{"row":2,"column":148},"end":{"row":2,"column":149},"action":"insert","lines":["a"]},{"start":{"row":2,"column":149},"end":{"row":2,"column":150},"action":"insert","lines":["m"]},{"start":{"row":2,"column":150},"end":{"row":2,"column":151},"action":"insert","lines":["e"]}],[{"start":{"row":2,"column":151},"end":{"row":2,"column":152},"action":"insert","lines":[" "],"id":237},{"start":{"row":2,"column":152},"end":{"row":2,"column":153},"action":"insert","lines":["L"]},{"start":{"row":2,"column":153},"end":{"row":2,"column":154},"action":"insert","lines":["I"]}],[{"start":{"row":2,"column":154},"end":{"row":2,"column":155},"action":"insert","lines":["K"],"id":238},{"start":{"row":2,"column":155},"end":{"row":2,"column":156},"action":"insert","lines":["E"]}],[{"start":{"row":2,"column":156},"end":{"row":2,"column":157},"action":"insert","lines":[" "],"id":239}],[{"start":{"row":2,"column":157},"end":{"row":2,"column":158},"action":"insert","lines":["\""],"id":240}],[{"start":{"row":2,"column":157},"end":{"row":2,"column":158},"action":"remove","lines":["\""],"id":241}],[{"start":{"row":2,"column":157},"end":{"row":2,"column":158},"action":"insert","lines":["'"],"id":242}],[{"start":{"row":2,"column":158},"end":{"row":2,"column":175},"action":"insert","lines":["Young Latin Girls"],"id":243}],[{"start":{"row":2,"column":175},"end":{"row":2,"column":176},"action":"insert","lines":["%"],"id":244},{"start":{"row":2,"column":176},"end":{"row":2,"column":177},"action":"insert","lines":["'"]}],[{"start":{"row":4,"column":0},"end":{"row":6,"column":0},"action":"remove","lines":["Get all the distinct actors ids who acted in all movie whose title starts ","with Young Latin Girls.",""],"id":245}],[{"start":{"row":2,"column":30},"end":{"row":2,"column":31},"action":"remove","lines":["`"],"id":246}],[{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"insert","lines":["r"],"id":247},{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"insert","lines":["`"]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":88},"action":"insert","lines":["How many distinct actors have acted in any movie between 1990 and 2000 (both inclusive)."],"id":248}],[{"start":{"row":5,"column":43},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":249}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["Q"],"id":250},{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["4"]},{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["="]}],[{"start":{"row":3,"column":3},"end":{"row":3,"column":5},"action":"insert","lines":["''"],"id":251}],[{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["'"],"id":252}],[{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"remove","lines":["'"],"id":253},{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"remove","lines":["'"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":6},"action":"insert","lines":["''"],"id":254}],[{"start":{"row":3,"column":6},"end":{"row":3,"column":180},"action":"insert","lines":["SELECT DISTINCT(`Actor`.id) FROM (Actor INNER JOIN Cast on `Cast`.pid = `Actor`.id) INNER JOIN Movie on `Movie`.id = `Cast`.mid WHERE `Movie`.name LIKE 'Young Latin Girls%';'"],"id":255}],[{"start":{"row":3,"column":180},"end":{"row":3,"column":181},"action":"insert","lines":["'"],"id":256},{"start":{"row":3,"column":181},"end":{"row":3,"column":182},"action":"insert","lines":["'"]}],[{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":[" "],"id":257},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["C"]}],[{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["O"],"id":258},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["U"]}],[{"start":{"row":3,"column":22},"end":{"row":3,"column":25},"action":"remove","lines":["COU"],"id":259},{"start":{"row":3,"column":22},"end":{"row":3,"column":27},"action":"insert","lines":["COUNT"]}],[{"start":{"row":3,"column":183},"end":{"row":3,"column":184},"action":"remove","lines":["'"],"id":260},{"start":{"row":3,"column":182},"end":{"row":3,"column":183},"action":"remove","lines":["%"]},{"start":{"row":3,"column":181},"end":{"row":3,"column":182},"action":"remove","lines":["s"]},{"start":{"row":3,"column":180},"end":{"row":3,"column":181},"action":"remove","lines":["l"]},{"start":{"row":3,"column":179},"end":{"row":3,"column":180},"action":"remove","lines":["r"]},{"start":{"row":3,"column":178},"end":{"row":3,"column":179},"action":"remove","lines":["i"]},{"start":{"row":3,"column":177},"end":{"row":3,"column":178},"action":"remove","lines":["G"]},{"start":{"row":3,"column":176},"end":{"row":3,"column":177},"action":"remove","lines":[" "]},{"start":{"row":3,"column":175},"end":{"row":3,"column":176},"action":"remove","lines":["n"]},{"start":{"row":3,"column":174},"end":{"row":3,"column":175},"action":"remove","lines":["i"]},{"start":{"row":3,"column":173},"end":{"row":3,"column":174},"action":"remove","lines":["t"]},{"start":{"row":3,"column":172},"end":{"row":3,"column":173},"action":"remove","lines":["a"]},{"start":{"row":3,"column":171},"end":{"row":3,"column":172},"action":"remove","lines":["L"]},{"start":{"row":3,"column":170},"end":{"row":3,"column":171},"action":"remove","lines":[" "]},{"start":{"row":3,"column":169},"end":{"row":3,"column":170},"action":"remove","lines":["g"]},{"start":{"row":3,"column":168},"end":{"row":3,"column":169},"action":"remove","lines":["n"]},{"start":{"row":3,"column":167},"end":{"row":3,"column":168},"action":"remove","lines":["u"]}],[{"start":{"row":3,"column":166},"end":{"row":3,"column":167},"action":"remove","lines":["o"],"id":261},{"start":{"row":3,"column":165},"end":{"row":3,"column":166},"action":"remove","lines":["Y"]},{"start":{"row":3,"column":164},"end":{"row":3,"column":165},"action":"remove","lines":["'"]},{"start":{"row":3,"column":163},"end":{"row":3,"column":164},"action":"remove","lines":[" "]},{"start":{"row":3,"column":162},"end":{"row":3,"column":163},"action":"remove","lines":["E"]}],[{"start":{"row":3,"column":161},"end":{"row":3,"column":162},"action":"remove","lines":["K"],"id":262},{"start":{"row":3,"column":160},"end":{"row":3,"column":161},"action":"remove","lines":["I"]},{"start":{"row":3,"column":159},"end":{"row":3,"column":160},"action":"remove","lines":["L"]},{"start":{"row":3,"column":158},"end":{"row":3,"column":159},"action":"remove","lines":[" "]},{"start":{"row":3,"column":157},"end":{"row":3,"column":158},"action":"remove","lines":["e"]},{"start":{"row":3,"column":156},"end":{"row":3,"column":157},"action":"remove","lines":["m"]},{"start":{"row":3,"column":155},"end":{"row":3,"column":156},"action":"remove","lines":["a"]},{"start":{"row":3,"column":154},"end":{"row":3,"column":155},"action":"remove","lines":["n"]}],[{"start":{"row":3,"column":154},"end":{"row":3,"column":155},"action":"insert","lines":["y"],"id":263},{"start":{"row":3,"column":155},"end":{"row":3,"column":156},"action":"insert","lines":["e"]},{"start":{"row":3,"column":156},"end":{"row":3,"column":157},"action":"insert","lines":["a"]},{"start":{"row":3,"column":157},"end":{"row":3,"column":158},"action":"insert","lines":["r"]}],[{"start":{"row":3,"column":158},"end":{"row":3,"column":159},"action":"insert","lines":[" "],"id":264}],[{"start":{"row":3,"column":159},"end":{"row":3,"column":160},"action":"insert","lines":["B"],"id":265},{"start":{"row":3,"column":160},"end":{"row":3,"column":161},"action":"insert","lines":["e"]},{"start":{"row":3,"column":161},"end":{"row":3,"column":162},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":161},"end":{"row":3,"column":162},"action":"remove","lines":["t"],"id":266},{"start":{"row":3,"column":160},"end":{"row":3,"column":161},"action":"remove","lines":["e"]}],[{"start":{"row":3,"column":160},"end":{"row":3,"column":161},"action":"insert","lines":["E"],"id":267},{"start":{"row":3,"column":161},"end":{"row":3,"column":162},"action":"insert","lines":["T"]},{"start":{"row":3,"column":162},"end":{"row":3,"column":163},"action":"insert","lines":["W"]},{"start":{"row":3,"column":163},"end":{"row":3,"column":164},"action":"insert","lines":["E"]},{"start":{"row":3,"column":164},"end":{"row":3,"column":165},"action":"insert","lines":["E"]}],[{"start":{"row":3,"column":165},"end":{"row":3,"column":166},"action":"insert","lines":["N"],"id":268}],[{"start":{"row":3,"column":166},"end":{"row":3,"column":167},"action":"insert","lines":[" "],"id":269}],[{"start":{"row":3,"column":167},"end":{"row":3,"column":168},"action":"insert","lines":["1"],"id":270},{"start":{"row":3,"column":168},"end":{"row":3,"column":169},"action":"insert","lines":["9"]},{"start":{"row":3,"column":169},"end":{"row":3,"column":170},"action":"insert","lines":["9"]},{"start":{"row":3,"column":170},"end":{"row":3,"column":171},"action":"insert","lines":["0"]}],[{"start":{"row":3,"column":171},"end":{"row":3,"column":172},"action":"insert","lines":[","],"id":271},{"start":{"row":3,"column":172},"end":{"row":3,"column":173},"action":"insert","lines":["2"]},{"start":{"row":3,"column":173},"end":{"row":3,"column":174},"action":"insert","lines":["0"]},{"start":{"row":3,"column":174},"end":{"row":3,"column":175},"action":"insert","lines":["0"]}],[{"start":{"row":3,"column":175},"end":{"row":3,"column":176},"action":"insert","lines":["0"],"id":272}],[{"start":{"row":3,"column":167},"end":{"row":3,"column":168},"action":"insert","lines":["("],"id":273}],[{"start":{"row":3,"column":177},"end":{"row":3,"column":178},"action":"insert","lines":[")"],"id":274}],[{"start":{"row":3,"column":172},"end":{"row":3,"column":173},"action":"remove","lines":[","],"id":275}],[{"start":{"row":3,"column":172},"end":{"row":3,"column":173},"action":"insert","lines":[" "],"id":276},{"start":{"row":3,"column":173},"end":{"row":3,"column":174},"action":"insert","lines":["a"]},{"start":{"row":3,"column":174},"end":{"row":3,"column":175},"action":"insert","lines":["n"]}],[{"start":{"row":3,"column":175},"end":{"row":3,"column":176},"action":"insert","lines":["d"],"id":277}],[{"start":{"row":3,"column":176},"end":{"row":3,"column":177},"action":"insert","lines":[" "],"id":278}],[{"start":{"row":3,"column":181},"end":{"row":3,"column":182},"action":"remove","lines":[")"],"id":279}],[{"start":{"row":3,"column":167},"end":{"row":3,"column":168},"action":"remove","lines":["("],"id":280}],[{"start":{"row":5,"column":0},"end":{"row":7,"column":0},"action":"remove","lines":["How many distinct actors have acted in any ","movie between 1990 and 2000 (both inclusive).",""],"id":281}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":175},"action":"insert","lines":["SELECT DISTINCT COUNT(`Actor`.id) FROM (Actor INNER JOIN Cast on `Cast`.pid = `Actor`.id) INNER JOIN Movie on `Movie`.id = `Cast`.mid WHERE `Movie`.year BETWEEN 1990 and 2000;"],"id":282}],[{"start":{"row":5,"column":174},"end":{"row":5,"column":175},"action":"remove","lines":[";"],"id":284},{"start":{"row":5,"column":173},"end":{"row":5,"column":174},"action":"remove","lines":["0"]},{"start":{"row":5,"column":172},"end":{"row":5,"column":173},"action":"remove","lines":["0"]},{"start":{"row":5,"column":171},"end":{"row":5,"column":172},"action":"remove","lines":["0"]},{"start":{"row":5,"column":170},"end":{"row":5,"column":171},"action":"remove","lines":["2"]},{"start":{"row":5,"column":169},"end":{"row":5,"column":170},"action":"remove","lines":[" "]},{"start":{"row":5,"column":168},"end":{"row":5,"column":169},"action":"remove","lines":["d"]},{"start":{"row":5,"column":167},"end":{"row":5,"column":168},"action":"remove","lines":["n"]},{"start":{"row":5,"column":166},"end":{"row":5,"column":167},"action":"remove","lines":["a"]},{"start":{"row":5,"column":165},"end":{"row":5,"column":166},"action":"remove","lines":[" "]},{"start":{"row":5,"column":164},"end":{"row":5,"column":165},"action":"remove","lines":["0"]},{"start":{"row":5,"column":163},"end":{"row":5,"column":164},"action":"remove","lines":["9"]},{"start":{"row":5,"column":162},"end":{"row":5,"column":163},"action":"remove","lines":["9"]},{"start":{"row":5,"column":161},"end":{"row":5,"column":162},"action":"remove","lines":["1"]},{"start":{"row":5,"column":160},"end":{"row":5,"column":161},"action":"remove","lines":[" "]},{"start":{"row":5,"column":159},"end":{"row":5,"column":160},"action":"remove","lines":["N"]},{"start":{"row":5,"column":158},"end":{"row":5,"column":159},"action":"remove","lines":["E"]}],[{"start":{"row":5,"column":157},"end":{"row":5,"column":158},"action":"remove","lines":["E"],"id":285},{"start":{"row":5,"column":156},"end":{"row":5,"column":157},"action":"remove","lines":["W"]},{"start":{"row":5,"column":155},"end":{"row":5,"column":156},"action":"remove","lines":["T"]},{"start":{"row":5,"column":154},"end":{"row":5,"column":155},"action":"remove","lines":["E"]},{"start":{"row":5,"column":153},"end":{"row":5,"column":154},"action":"remove","lines":["B"]},{"start":{"row":5,"column":152},"end":{"row":5,"column":153},"action":"remove","lines":[" "]},{"start":{"row":5,"column":151},"end":{"row":5,"column":152},"action":"remove","lines":["r"]},{"start":{"row":5,"column":150},"end":{"row":5,"column":151},"action":"remove","lines":["a"]},{"start":{"row":5,"column":149},"end":{"row":5,"column":150},"action":"remove","lines":["e"]},{"start":{"row":5,"column":148},"end":{"row":5,"column":149},"action":"remove","lines":["y"]},{"start":{"row":5,"column":147},"end":{"row":5,"column":148},"action":"remove","lines":["."]},{"start":{"row":5,"column":146},"end":{"row":5,"column":147},"action":"remove","lines":["`"]},{"start":{"row":5,"column":145},"end":{"row":5,"column":146},"action":"remove","lines":["e"]},{"start":{"row":5,"column":144},"end":{"row":5,"column":145},"action":"remove","lines":["i"]},{"start":{"row":5,"column":143},"end":{"row":5,"column":144},"action":"remove","lines":["v"]},{"start":{"row":5,"column":142},"end":{"row":5,"column":143},"action":"remove","lines":["o"]},{"start":{"row":5,"column":141},"end":{"row":5,"column":142},"action":"remove","lines":["M"]},{"start":{"row":5,"column":140},"end":{"row":5,"column":141},"action":"remove","lines":["`"]},{"start":{"row":5,"column":139},"end":{"row":5,"column":140},"action":"remove","lines":[" "]},{"start":{"row":5,"column":138},"end":{"row":5,"column":139},"action":"remove","lines":["E"]}],[{"start":{"row":5,"column":137},"end":{"row":5,"column":138},"action":"remove","lines":["R"],"id":286},{"start":{"row":5,"column":136},"end":{"row":5,"column":137},"action":"remove","lines":["E"]},{"start":{"row":5,"column":135},"end":{"row":5,"column":136},"action":"remove","lines":["H"]},{"start":{"row":5,"column":134},"end":{"row":5,"column":135},"action":"remove","lines":["W"]},{"start":{"row":5,"column":133},"end":{"row":5,"column":134},"action":"remove","lines":[" "]},{"start":{"row":5,"column":132},"end":{"row":5,"column":133},"action":"remove","lines":["d"]},{"start":{"row":5,"column":131},"end":{"row":5,"column":132},"action":"remove","lines":["i"]},{"start":{"row":5,"column":130},"end":{"row":5,"column":131},"action":"remove","lines":["m"]},{"start":{"row":5,"column":129},"end":{"row":5,"column":130},"action":"remove","lines":["."]},{"start":{"row":5,"column":128},"end":{"row":5,"column":129},"action":"remove","lines":["`"]},{"start":{"row":5,"column":127},"end":{"row":5,"column":128},"action":"remove","lines":["t"]},{"start":{"row":5,"column":126},"end":{"row":5,"column":127},"action":"remove","lines":["s"]},{"start":{"row":5,"column":125},"end":{"row":5,"column":126},"action":"remove","lines":["a"]},{"start":{"row":5,"column":124},"end":{"row":5,"column":125},"action":"remove","lines":["C"]},{"start":{"row":5,"column":123},"end":{"row":5,"column":124},"action":"remove","lines":["`"]},{"start":{"row":5,"column":122},"end":{"row":5,"column":123},"action":"remove","lines":[" "]},{"start":{"row":5,"column":121},"end":{"row":5,"column":122},"action":"remove","lines":["="]},{"start":{"row":5,"column":120},"end":{"row":5,"column":121},"action":"remove","lines":[" "]}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"remove","lines":["SELECT DISTINCT COUNT(`Actor`.id) FROM (Actor INNER JOIN Cast on `Cast`.pid = `Actor`.id) INNER JOIN Movie on `Movie`.id",""],"id":287}],[{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["("],"id":288}],[{"start":{"row":3,"column":40},"end":{"row":3,"column":41},"action":"insert","lines":[")"],"id":289}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":88},"action":"insert","lines":["How many distinct actors have acted in any movie between 1990 and 2000 (both inclusive)."],"id":291}],[{"start":{"row":3,"column":155},"end":{"row":3,"column":156},"action":"remove","lines":["."],"id":292},{"start":{"row":3,"column":154},"end":{"row":3,"column":155},"action":"remove","lines":["`"]},{"start":{"row":3,"column":153},"end":{"row":3,"column":154},"action":"remove","lines":["e"]},{"start":{"row":3,"column":152},"end":{"row":3,"column":153},"action":"remove","lines":["i"]},{"start":{"row":3,"column":151},"end":{"row":3,"column":152},"action":"remove","lines":["v"]},{"start":{"row":3,"column":150},"end":{"row":3,"column":151},"action":"remove","lines":["o"]},{"start":{"row":3,"column":149},"end":{"row":3,"column":150},"action":"remove","lines":["M"]},{"start":{"row":3,"column":148},"end":{"row":3,"column":149},"action":"remove","lines":["`"]}],[{"start":{"row":3,"column":41},"end":{"row":3,"column":42},"action":"remove","lines":[" "],"id":293},{"start":{"row":3,"column":40},"end":{"row":3,"column":41},"action":"remove","lines":[")"]}],[{"start":{"row":3,"column":29},"end":{"row":3,"column":37},"action":"insert","lines":["DISTINCT"],"id":294}],[{"start":{"row":3,"column":37},"end":{"row":3,"column":38},"action":"insert","lines":[" "],"id":295}],[{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"remove","lines":["("],"id":296},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"remove","lines":[" "]},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"remove","lines":["T"]},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"remove","lines":["C"]},{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"remove","lines":["N"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"remove","lines":["I"]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"remove","lines":["T"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"remove","lines":["S"]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"remove","lines":["I"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"remove","lines":["D"]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":88},"action":"remove","lines":["How many distinct actors have acted in any movie between 1990 and 2000 (both inclusive)."],"id":297}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":470.31827206342007,"selection":{"start":{"row":2,"column":171},"end":{"row":2,"column":171},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1588916872680,"hash":"ba899fe12939149c6a7e114ded4f3c313a5c06bb"}