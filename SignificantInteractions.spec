/*
A KBase module: SignificantInteractions
*/

module SignificantInteractions {
    typedef structure {
        string MatrixIds;
        float sig_cutoff;
        float corr_cutoff;
        int frequency;
        string search_for_type;
        string matrix_unique_to;
        string corr_matrix_name;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_SignificantInteractions(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
