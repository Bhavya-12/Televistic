#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    fstream f,f1;
    f1.open("output1.txt",ios::app);
    f.open("englishmovies.txt",ios::in);
    string moviename,hero,director,yor,murl,imgurl,genre,rating,query,language,heroine,gender;
    string mvid ,acid ,dirid,acsid;
    int index;
    cout << "Enter index value : ";
    cin >> index;
    while(!f.eof())
    {
        getline(f,moviename);
        getline(f,hero);
        getline(f,heroine);
        getline(f,director);
        getline(f,yor);
        getline(f,language);
        getline(f,murl);
        getline(f,imgurl);
        getline(f,rating);
        getline(f,genre);
        getline(f,gender);
        index++;
        if(index<10)
            mvid = "M000"+ to_string(index);
        else if(index>=10 && index<100)
            mvid = "M00"+to_string(index);
        else if(index>=100 && index<1000)
            mvid = "M0"+to_string(index);
        else
            mvid = "M"+to_string(index);
        if(index<10)
            acid = "AC000"+ to_string(index);
        else if(index>=10 && index<100)
            acid = "AC00"+to_string(index);
        else if(index>=100 && index<1000)
            acid = "AC0"+to_string(index);
        else
            acid = "AC"+to_string(index);
        if(index<10)
            acsid = "AC000"+ to_string(++index);
        else if(index>=10 && index<100)
            acsid = "AC00"+to_string(++index);
        else if(index>=100 && index<1000)
            acsid = "AC0"+to_string(++index);
        else
            acsid = "AC"+to_string(++index);    
          if(index<10)
            dirid = "G000"+ to_string(index);
        else if(index>=10 && index<100)
            dirid = "G00"+to_string(index);
        else if(index>=100 && index<1000)
            dirid = "G0"+to_string(index);
        else
            dirid = "G"+to_string(index);    
        query = "Insert into Movies values('"+mvid+"','"+moviename+"','"+language+"',"+rating+",'"+murl+"','"+imgurl+"','"+dirid+"','');";
        string query2 = "Insert into Actors values('"+acid+"','"+hero+"','M');";
        string query6 = "Insert into Actors values('"+acsid+"','"+heroine+"','F');";
        string query3 = "Insert into Movie_Director values('"+director+"','"+gender+"','"+yor+"','"+mvid+"');";
        string query4 = "Insert into Movie_Actor values('"+acid+"','"+mvid+"');";
         string query7 = "Insert into Movie_Actor values('"+acsid+"','"+mvid+"');";
        string query5 = "Insert into Genre values('"+dirid+"','"+genre+"');";
      
        f1 << query2 << "\n";
        f1 << query6 << "\n";
        f1 << query5 << "\n";
        f1 << query << "\n";
        f1 << query3 << "\n";
        f1 << query4 << "\n";
        f1 << query7 << "\n";
        
    }
    f1.close();
    f.close();
}