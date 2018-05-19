UPDATE public.empresa
   SET emp_endemp='R. José Olímpio, 191 - Messejana, Fortaleza/CE, 60873-250' , 
       emp_telemp='08532994100'       
 WHERE emp_codemp = '02';
 
UPDATE public.empresa
   SET emp_endemp='R. Prof. Leite Gondim - Antônio Bezerra, Fort./CE, 60020-181' , 
       emp_telemp='08532352133'       
 WHERE emp_codemp = '03';

UPDATE public.loja
   SET loj_endloj='R. José Olímpio', 
       loj_telloj='32994100', 
       loj_dddloj='085', 
       loj_numero='191', 
       loj_bailoj='Messejana', 
       loj_ufloj='CE', 
       loj_cidloj='Fortaleza', 
       loj_ceploj='60873250'
 WHERE loj_codloj='00002';


UPDATE public.loja
   SET loj_endloj='Rua Professor Leite Gondim', 
       loj_telloj='32352133', 
       loj_dddloj='501', 
       loj_numero='579', 
       loj_bailoj='Antônio Bezerra', 
       loj_ufloj='CE', 
       loj_cidloj='Fortaleza', 
       loj_ceploj='60020181'
 WHERE loj_codloj='00003';