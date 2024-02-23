nt Table[6][3]={ {1,2,2},
{ 1,3,3},{4,4,2}, {5,5,5},
{ 4,4,4}, {4,4,4} };
int state=0, i=0, col=0;
// start at state 0
string w=”abbcc$”;
while ( i < w.length() )
{ switch( w[i] )
{ case ‘a’ : col=0; break;
case ‘b’ : col=1; break;
case ‘c’ : col=2; break;
case ‘$’:
if (state==2||state==5)
cout<<w<<” accepted”;
else
cout<<w<<” rejected”;
break;
}//end of switch
//go to the next state
state= Table[state][col];
//go to the next input letter
++i;
}// end of while