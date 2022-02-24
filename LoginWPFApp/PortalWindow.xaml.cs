using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace LoginWPFApp
{
    /// <summary>
    /// Interaction logic for PortalWindow.xaml
    /// </summary>
    public partial class PortalWindow : Window
    {
        private string youtube = "https://youtube.com";
        private string google = "https://google.com";
        private string aws = "https://aws.amazon.com";
        private string github = "https://github.com";

        public PortalWindow()
        {
            InitializeComponent();
        }

        private void Link_1_Button_Click(object sender, RoutedEventArgs e)
        {
            System.Diagnostics.Process.Start(youtube);
        }

        private void Link_2_Button_Click(object sender, RoutedEventArgs e)
        {
            System.Diagnostics.Process.Start(google);
        }

        private void Link_3_Button_Click(object sender, RoutedEventArgs e)
        {
            System.Diagnostics.Process.Start(aws);
        }

        private void Link_4_Button_Click(object sender, RoutedEventArgs e)
        {
            System.Diagnostics.Process.Start(github);
        }

        private void ExitButton_Click(object sender, RoutedEventArgs e)
        {
            Application.Current.Shutdown();
        }
    }
}
