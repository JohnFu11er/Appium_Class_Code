   M S B A M L   `   `   `  ����F  BLoginWPFApp, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null)clr-namespace:LoginWPFAppLoginWPFApp  5   	   $    LoginWPFApp.VerificationWindow   5   	   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   +localclr-namespace:LoginWPFApp     5   	     � Title$  VerificationWindow��5   	   $	��300��6$   $	��400��61    � WindowStyle$
 None=�5	   	    � 
ResizeMode$ NoResize=�6   .��5
      � ��5   
   �� 5       �� 
StartPoint$ 0.1,0&�6"    �� EndPoint$ 0.9,1&�65   .��5      �  � Color$ 
DodgerBlue��6    � Offset$ 1Q�62   � 5      $ 
BlueViolet��6   $ 0Q�62   5      .+�5   
   �� $	��260��6   $	��Top=�6    �� CornerRadius$ 0 0 0 0��66   
�������6f   �� 5   
    �� Orientation$ 
Horizontal=�6   .+�5      �� $	��300��6   .+�5      �� $��20 40q�6   .+�5      �� $��Verification��6    $��20q�64   
�������$��38(�6S   	 �� TextAlignment$	 Center=�6a   6z   �� 5      $ 
Horizontal=�6!   $��10q�6:   .+�5      �� $��Verification Code��6$   
�������6R   �� 5      -   5        
 ��Name$
 authTxt��5   H   4  .System.Windows.Automation.AutomationProperties   AutomationId$ 9��6"   
������� �� 
CaretBrush
 ��+�� �� SelectionBrush
 ����$
��10 0q�6�   $	��250��6�   
�������
���   �6�   5      �� 5      $��15,10,-100,10q�6!   $ 
Horizontal=�68   $��Center=�6Q   $	��335��6n   .+�5       �� -   5         ��Name$ loginButton��5    �   $ 10��6!   $��90��6H   $��30��6S   $��50 0 0 0q�6_   
������
������� � ToolTip$ Login��6�   $��Login��6�   6�   �� 5!      -   5        $ 
backbutton��5!   �   $ 11��6!   
�������
������$��20 0 0 0q�6s   $��90��6�   $��30��6�   $ Back to Main��6�   $��Back to Main��6�   6�   5"      5$      5%      5'      5(      5)      