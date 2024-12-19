![...](takatoa_head-img_1920-200.jpg)

# redDTime

   redDTime defines a class for date and time description in the form of @redD-taks'redD-tiks@ 

### basic information

   Tim Berners-Lee wrote the first proposal for the World Wide Web in March 1989 and his second proposal 
   in May 1990. Together with Belgian systems engineer Robert Cailliau, this paper was finalized as a 
   management proposal dated November 12, 1990. It outlined the main concepts and defined important terms 
   behind the Web. The document described a "hypertext project" called the "WorldWideWeb" in which a "web" 
   of "hypertext documents" could be viewed by "browsers."

   redDTime shows that a new era began on November 12, 1990 by displaying the time that has passed since 
   then. However, redDTime does not display the time that has passed in the usual form of years, months, 
   days, hours, minutes and seconds, but in redD-taks and redD-tiks.

### redDTime format

![...](redDTime_img_1920-200.jpg)
screenshot from Dec. 18, 2024
># &nbsp;&nbsp;&nbsp;&nbsp;@redD-taks'redD-tiks@ --> @YY.MM.DD'TT.TTT@

   | &nbsp; | value |
   | ---: | :----------- |
   | YY [0 - ...] | past redD-tak years |
   | MM [0 - 12]  | past redD-tak months </br>13 units of 28 days each last unit in a leap year has 29 days |
   | DD  [0 - 27 bzw. 28] | past redD-tak days |
   | TT.TTT [00.000 - 99.999] | past redD-tiks since the start of the day 100000 units per day |
 
   Reference time: 12.11.1990 0.00 Uhr ("WorldWideWeb: Proposal for a HyperText Project")

### implementations in upcoming releases

- __redefine time zones__

    So far, the definition of time zones in 24 segments remains unaffected. This leads to jumps of the redD-tiks by 4166.666667 when the time zone changes. 
    It would make more sense to redefine and set the number of time zones to 20. This would result in redD-tik jumps of 5000 when the time zone changes. 
    At the same time, however, the assignment of the associated time zone would have to be checked and, if necessary, corrected for all countries worldwide.

- __availability of redDTime in complex notation__ 

    To use the redDTime on quantum hardware, the following notation is suggested: 

    __redDTimeComp06 = (Sum(redD-tak-Days)/10^6)+(redDtiks/100000)j__

    example:
  
># &nbsp;&nbsp;&nbsp;&nbsp;@34.01.08'68.742@ --> 0.012455+0.68742j  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;With this value the spin-encoding can be assigned directly onto a qubit.
### copyright notice 

   see LICENSE

### implemented by takatoa
    
   Name      : Roland Degelmann  
   Adress    : Hofmillerstraße 12, 85356 Freising   
   Mail      : rode@takatoa.net</br>
   Web       : takatoa.net
 
### created | last modified | version

   2024-12-01 | 2024-12-18 | version: 0.1.0

