
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN BOOLEAN COLON COMMA DIV ELSE ELSEIF EQ ERROR FALSE FLOAT FLOATNUMBER FOR FUNCTION GE GT ID IF IN INTEGER INTEGERNUMBER LCB LE LRB LSB LT MAIN MOD MUL NE NOT ON OR PRINT RCB RETURN RRB RSB SEMICOLON SUB SUM TRUE WHERE WHILEprogram : declist MAIN LRB RRB block \n        | MAIN LRB RRB blockempty : \n        declist : dec \n        | declist dec \n        dec : vardec \n        | funcdec type : INTEGER \n        | FLOAT \n        | BOOLEANiddec : ID \n        | ID LSB exa RSB \n        | ID ASSIGN exaidlist : iddec \n        | idlist COMMA iddecvardec : idlist COLON type SEMICOLONfuncdec : FUNCTION ID LRB paramdecs RRB COLON type block \n        | FUNCTION ID  LRB paramdecs RRB blockparamdecs : paramdecslist \n        | emptyparamdecslist : paramdec\n        | paramdecslist COMMA paramdecparamdec : ID COLON type\n        | ID LSB RSB COLON typeblock : LCB RCBlvalue : ID\n        | ID LSB exa RSBoperator : SUM \n        | SUB\n        | MUL\n        | DIV\n        | MOD\n        | GT\n        | GE\n        | LT\n        | LE\n        | EQ\n        | NE\n        const :  INTEGERNUMBER\n        | FLOATNUMBER\n        | TRUE\n        | FALSE\n        exa : lvalue ASSIGN exa\n        | ex\n        ex : NOT ex \n        | ex1\n        ex1 : ex1 AND exp\n        | ex1 OR exp\n        | exp\n        exp : exp operator exp1\n        | exp1\n        exp1 : SUB exp1 \n        | exp2\n        exp2 : LRB exa RRB\n        | const\n        | ID LRB RRB\n        | ID LRB explist RRB\n        | lvalue\n        explist : exa\n        | explist COMMA exa\n        '
    
_lr_action_items = {'MAIN':([0,2,4,5,6,12,47,77,94,103,],[3,11,-4,-6,-7,-5,-16,-25,-18,-17,]),'FUNCTION':([0,2,4,5,6,12,47,77,94,103,],[8,8,-4,-6,-7,-5,-16,-25,-18,-17,]),'ID':([0,2,4,5,6,8,12,15,17,18,26,31,35,37,47,53,54,56,60,61,62,63,64,65,66,67,68,69,70,71,72,73,77,81,94,98,103,],[9,9,-4,-6,-7,16,-5,9,27,27,48,58,58,27,-16,27,27,27,58,58,58,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-25,48,-18,27,-17,]),'$end':([1,45,76,77,],[0,-2,-1,-25,]),'LRB':([3,11,16,17,18,27,31,35,37,53,54,56,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,98,],[13,19,26,37,37,54,37,37,37,37,37,37,54,37,37,37,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,37,]),'COLON':([7,9,10,25,27,29,30,32,33,34,36,38,39,40,41,42,43,48,55,57,58,59,74,80,83,86,87,88,89,90,92,96,97,],[14,-11,-14,-15,-26,-58,-44,-46,-49,-51,-53,-55,-39,-40,-41,-42,-13,78,-12,-45,-26,-58,-52,93,-56,-43,-47,-48,-50,-54,99,-27,-57,]),'COMMA':([7,9,10,22,23,24,25,27,29,30,32,33,34,36,38,39,40,41,42,43,50,52,55,57,58,59,74,83,84,85,86,87,88,89,90,91,95,96,97,101,102,],[15,-11,-14,-8,-9,-10,-15,-26,-58,-44,-46,-49,-51,-53,-55,-39,-40,-41,-42,-13,81,-21,-12,-45,-26,-58,-52,-56,98,-59,-43,-47,-48,-50,-54,-23,-22,-27,-57,-60,-24,]),'LSB':([9,27,48,58,],[17,53,79,53,]),'ASSIGN':([9,27,29,96,],[18,-26,56,-27,]),'RRB':([13,19,22,23,24,26,27,29,30,32,33,34,36,38,39,40,41,42,49,50,51,52,54,57,58,59,74,75,83,84,85,86,87,88,89,90,91,95,96,97,101,102,],[20,44,-8,-9,-10,-3,-26,-58,-44,-46,-49,-51,-53,-55,-39,-40,-41,-42,80,-19,-20,-21,83,-45,-26,-58,-52,90,-56,97,-59,-43,-47,-48,-50,-54,-23,-22,-27,-57,-60,-24,]),'INTEGER':([14,78,93,99,],[22,22,22,22,]),'FLOAT':([14,78,93,99,],[23,23,23,23,]),'BOOLEAN':([14,78,93,99,],[24,24,24,24,]),'NOT':([17,18,31,37,53,54,56,98,],[31,31,31,31,31,31,31,31,]),'SUB':([17,18,27,29,31,33,34,35,36,37,38,39,40,41,42,53,54,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,83,87,88,89,90,96,97,98,],[35,35,-26,-58,35,64,-51,35,-53,35,-55,-39,-40,-41,-42,35,35,35,-26,-58,35,35,35,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-52,-56,64,64,-50,-54,-27,-57,35,]),'INTEGERNUMBER':([17,18,31,35,37,53,54,56,60,61,62,63,64,65,66,67,68,69,70,71,72,73,98,],[39,39,39,39,39,39,39,39,39,39,39,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,39,]),'FLOATNUMBER':([17,18,31,35,37,53,54,56,60,61,62,63,64,65,66,67,68,69,70,71,72,73,98,],[40,40,40,40,40,40,40,40,40,40,40,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,40,]),'TRUE':([17,18,31,35,37,53,54,56,60,61,62,63,64,65,66,67,68,69,70,71,72,73,98,],[41,41,41,41,41,41,41,41,41,41,41,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,41,]),'FALSE':([17,18,31,35,37,53,54,56,60,61,62,63,64,65,66,67,68,69,70,71,72,73,98,],[42,42,42,42,42,42,42,42,42,42,42,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,42,]),'LCB':([20,22,23,24,44,80,100,],[46,-8,-9,-10,46,46,46,]),'SEMICOLON':([21,22,23,24,],[47,-8,-9,-10,]),'SUM':([27,29,33,34,36,38,39,40,41,42,58,59,74,83,87,88,89,90,96,97,],[-26,-58,63,-51,-53,-55,-39,-40,-41,-42,-26,-58,-52,-56,63,63,-50,-54,-27,-57,]),'MUL':([27,29,33,34,36,38,39,40,41,42,58,59,74,83,87,88,89,90,96,97,],[-26,-58,65,-51,-53,-55,-39,-40,-41,-42,-26,-58,-52,-56,65,65,-50,-54,-27,-57,]),'DIV':([27,29,33,34,36,38,39,40,41,42,58,59,74,83,87,88,89,90,96,97,],[-26,-58,66,-51,-53,-55,-39,-40,-41,-42,-26,-58,-52,-56,66,66,-50,-54,-27,-57,]),'MOD':([27,29,33,34,36,38,39,40,41,42,58,59,74,83,87,88,89,90,96,97,],[-26,-58,67,-51,-53,-55,-39,-40,-41,-42,-26,-58,-52,-56,67,67,-50,-54,-27,-57,]),'GT':([27,29,33,34,36,38,39,40,41,42,58,59,74,83,87,88,89,90,96,97,],[-26,-58,68,-51,-53,-55,-39,-40,-41,-42,-26,-58,-52,-56,68,68,-50,-54,-27,-57,]),'GE':([27,29,33,34,36,38,39,40,41,42,58,59,74,83,87,88,89,90,96,97,],[-26,-58,69,-51,-53,-55,-39,-40,-41,-42,-26,-58,-52,-56,69,69,-50,-54,-27,-57,]),'LT':([27,29,33,34,36,38,39,40,41,42,58,59,74,83,87,88,89,90,96,97,],[-26,-58,70,-51,-53,-55,-39,-40,-41,-42,-26,-58,-52,-56,70,70,-50,-54,-27,-57,]),'LE':([27,29,33,34,36,38,39,40,41,42,58,59,74,83,87,88,89,90,96,97,],[-26,-58,71,-51,-53,-55,-39,-40,-41,-42,-26,-58,-52,-56,71,71,-50,-54,-27,-57,]),'EQ':([27,29,33,34,36,38,39,40,41,42,58,59,74,83,87,88,89,90,96,97,],[-26,-58,72,-51,-53,-55,-39,-40,-41,-42,-26,-58,-52,-56,72,72,-50,-54,-27,-57,]),'NE':([27,29,33,34,36,38,39,40,41,42,58,59,74,83,87,88,89,90,96,97,],[-26,-58,73,-51,-53,-55,-39,-40,-41,-42,-26,-58,-52,-56,73,73,-50,-54,-27,-57,]),'AND':([27,29,32,33,34,36,38,39,40,41,42,58,59,74,83,87,88,89,90,96,97,],[-26,-58,60,-49,-51,-53,-55,-39,-40,-41,-42,-26,-58,-52,-56,-47,-48,-50,-54,-27,-57,]),'OR':([27,29,32,33,34,36,38,39,40,41,42,58,59,74,83,87,88,89,90,96,97,],[-26,-58,61,-49,-51,-53,-55,-39,-40,-41,-42,-26,-58,-52,-56,-47,-48,-50,-54,-27,-57,]),'RSB':([27,28,29,30,32,33,34,36,38,39,40,41,42,57,58,59,74,79,82,83,86,87,88,89,90,96,97,],[-26,55,-58,-44,-46,-49,-51,-53,-55,-39,-40,-41,-42,-45,-26,-58,-52,92,96,-56,-43,-47,-48,-50,-54,-27,-57,]),'RCB':([46,],[77,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declist':([0,],[2,]),'dec':([0,2,],[4,12,]),'vardec':([0,2,],[5,5,]),'funcdec':([0,2,],[6,6,]),'idlist':([0,2,],[7,7,]),'iddec':([0,2,15,],[10,10,25,]),'type':([14,78,93,99,],[21,91,100,102,]),'exa':([17,18,37,53,54,56,98,],[28,43,75,82,85,86,101,]),'lvalue':([17,18,31,35,37,53,54,56,60,61,62,98,],[29,29,59,59,29,29,29,29,59,59,59,29,]),'ex':([17,18,31,37,53,54,56,98,],[30,30,57,30,30,30,30,30,]),'ex1':([17,18,31,37,53,54,56,98,],[32,32,32,32,32,32,32,32,]),'exp':([17,18,31,37,53,54,56,60,61,98,],[33,33,33,33,33,33,33,87,88,33,]),'exp1':([17,18,31,35,37,53,54,56,60,61,62,98,],[34,34,34,74,34,34,34,34,34,34,89,34,]),'exp2':([17,18,31,35,37,53,54,56,60,61,62,98,],[36,36,36,36,36,36,36,36,36,36,36,36,]),'const':([17,18,31,35,37,53,54,56,60,61,62,98,],[38,38,38,38,38,38,38,38,38,38,38,38,]),'block':([20,44,80,100,],[45,76,94,103,]),'paramdecs':([26,],[49,]),'paramdecslist':([26,],[50,]),'empty':([26,],[51,]),'paramdec':([26,81,],[52,95,]),'operator':([33,87,88,],[62,62,62,]),'explist':([54,],[84,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declist MAIN LRB RRB block','program',5,'p_program','parser.py',19),
  ('program -> MAIN LRB RRB block','program',4,'p_program','parser.py',20),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',26),
  ('declist -> dec','declist',1,'p_declist_to_dec','parser.py',35),
  ('declist -> declist dec','declist',2,'p_declist_to_dec','parser.py',36),
  ('dec -> vardec','dec',1,'p_dec_to_var_or_func','parser.py',42),
  ('dec -> funcdec','dec',1,'p_dec_to_var_or_func','parser.py',43),
  ('type -> INTEGER','type',1,'p_type_to_type','parser.py',48),
  ('type -> FLOAT','type',1,'p_type_to_type','parser.py',49),
  ('type -> BOOLEAN','type',1,'p_type_to_type','parser.py',50),
  ('iddec -> ID','iddec',1,'p_iddec_to_id','parser.py',55),
  ('iddec -> ID LSB exa RSB','iddec',4,'p_iddec_to_id','parser.py',56),
  ('iddec -> ID ASSIGN exa','iddec',3,'p_iddec_to_id','parser.py',57),
  ('idlist -> iddec','idlist',1,'p_idlist_to_iddec','parser.py',62),
  ('idlist -> idlist COMMA iddec','idlist',3,'p_idlist_to_iddec','parser.py',63),
  ('vardec -> idlist COLON type SEMICOLON','vardec',4,'p_vardec_to_idlist_and_tyep','parser.py',68),
  ('funcdec -> FUNCTION ID LRB paramdecs RRB COLON type block','funcdec',8,'p_funcdec_to_dec','parser.py',73),
  ('funcdec -> FUNCTION ID LRB paramdecs RRB block','funcdec',6,'p_funcdec_to_dec','parser.py',74),
  ('paramdecs -> paramdecslist','paramdecs',1,'p_paramdecs_to_paramdecslist','parser.py',80),
  ('paramdecs -> empty','paramdecs',1,'p_paramdecs_to_paramdecslist','parser.py',81),
  ('paramdecslist -> paramdec','paramdecslist',1,'p_paramdecslist_to_paramdec','parser.py',86),
  ('paramdecslist -> paramdecslist COMMA paramdec','paramdecslist',3,'p_paramdecslist_to_paramdec','parser.py',87),
  ('paramdec -> ID COLON type','paramdec',3,'p_paramdec_to_id','parser.py',91),
  ('paramdec -> ID LSB RSB COLON type','paramdec',5,'p_paramdec_to_id','parser.py',92),
  ('block -> LCB RCB','block',2,'p_block_to_statement','parser.py',95),
  ('lvalue -> ID','lvalue',1,'p_lvalue','parser.py',100),
  ('lvalue -> ID LSB exa RSB','lvalue',4,'p_lvalue','parser.py',101),
  ('operator -> SUM','operator',1,'p_opertor','parser.py',105),
  ('operator -> SUB','operator',1,'p_opertor','parser.py',106),
  ('operator -> MUL','operator',1,'p_opertor','parser.py',107),
  ('operator -> DIV','operator',1,'p_opertor','parser.py',108),
  ('operator -> MOD','operator',1,'p_opertor','parser.py',109),
  ('operator -> GT','operator',1,'p_opertor','parser.py',110),
  ('operator -> GE','operator',1,'p_opertor','parser.py',111),
  ('operator -> LT','operator',1,'p_opertor','parser.py',112),
  ('operator -> LE','operator',1,'p_opertor','parser.py',113),
  ('operator -> EQ','operator',1,'p_opertor','parser.py',114),
  ('operator -> NE','operator',1,'p_opertor','parser.py',115),
  ('const -> INTEGERNUMBER','const',1,'p_const','parser.py',126),
  ('const -> FLOATNUMBER','const',1,'p_const','parser.py',127),
  ('const -> TRUE','const',1,'p_const','parser.py',128),
  ('const -> FALSE','const',1,'p_const','parser.py',129),
  ('exa -> lvalue ASSIGN exa','exa',3,'p_ex_assign','parser.py',138),
  ('exa -> ex','exa',1,'p_ex_assign','parser.py',139),
  ('ex -> NOT ex','ex',2,'p_ex','parser.py',144),
  ('ex -> ex1','ex',1,'p_ex','parser.py',145),
  ('ex1 -> ex1 AND exp','ex1',3,'p_ex1','parser.py',150),
  ('ex1 -> ex1 OR exp','ex1',3,'p_ex1','parser.py',151),
  ('ex1 -> exp','ex1',1,'p_ex1','parser.py',152),
  ('exp -> exp operator exp1','exp',3,'p_exp','parser.py',157),
  ('exp -> exp1','exp',1,'p_exp','parser.py',158),
  ('exp1 -> SUB exp1','exp1',2,'p_exp1','parser.py',163),
  ('exp1 -> exp2','exp1',1,'p_exp1','parser.py',164),
  ('exp2 -> LRB exa RRB','exp2',3,'p_exp2','parser.py',169),
  ('exp2 -> const','exp2',1,'p_exp2','parser.py',170),
  ('exp2 -> ID LRB RRB','exp2',3,'p_exp2','parser.py',171),
  ('exp2 -> ID LRB explist RRB','exp2',4,'p_exp2','parser.py',172),
  ('exp2 -> lvalue','exp2',1,'p_exp2','parser.py',173),
  ('explist -> exa','explist',1,'p_explist','parser.py',177),
  ('explist -> explist COMMA exa','explist',3,'p_explist','parser.py',178),
]
