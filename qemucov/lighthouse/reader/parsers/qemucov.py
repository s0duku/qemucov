
import collections
from ..coverage_file import CoverageFile


class QemucovModule:
    def __init__(self,module_id,module_start,module_end,module_file):
        self.module_id = module_id
        self.module_start = module_start
        self.module_end = module_end
        self.module_file = module_file

class QemucovData(CoverageFile):
    """
    Qemucov covrage file parser
    """

    def __init__(self,filepath):
        self.filepath = filepath
        self.modules = {}
        self.bbs = {}
        super(QemucovData, self).__init__(filepath)


    #--------------------------------------------------------------------------
    # Public
    #--------------------------------------------------------------------------

    def get_offsets(self, module_name):
        """
        Return coverage data as basic block offsets for the named module.
        """
        mod = self.modules.get(module_name)
        if mod == None:
            return []

        cov_blocks = self.bbs.get(str(mod.module_id))

        if cov_blocks == None:
            return []

        return cov_blocks
    #--------------------------------------------------------------------------
    # Parsing Routines - Top Level
    #--------------------------------------------------------------------------
    
    def _parse(self):
        """
        Parse qemucov coverage from the given log file.
        """
        
        with open(self.filepath, "rb") as f:
            self._parse_cov_header(f)
            self._parse_cov_module_table(f)
            self._parse_cov_bb_table(f)


    def _parse_cov_header(self,f):
        tmp_line = f.readline().decode('utf-8').strip().split(":")
        if tmp_line[0] != "QEMUCOV_COV VERSION":
            raise ValueError("Invalid Qemucov Format!")
        self.version = int(tmp_line[1])
        tmp_line = f.readline().decode('utf-8').strip().split(":")[1]
        tmp_line = tmp_line.split(",")[1].strip()
        self.module_count = int(tmp_line.split(" ")[1].strip())
        f.readline()


    def _parse_cov_module_table(self,f):
        for i in range(self.module_count):
            tmp_line = f.readline().decode('utf-8').strip()
            tmp_line = tmp_line.split(",")

            module_id = int(tmp_line[0].strip())
            module_start = int(tmp_line[1].strip(),16)
            module_end = int(tmp_line[2].strip(),16)
            module_file = tmp_line[6].strip()
            
            mod = QemucovModule(module_id,module_start,module_end,module_file)
            self.modules[module_file] = mod


    def _parse_cov_bb_table(self,f):
        f.readline()
        tmp_line = f.readline().decode('utf-8').strip()

        while tmp_line:
            tmp_line = tmp_line.split(',')
            mod_id = str(int(tmp_line[0].strip()))
            bb_start = int(tmp_line[1].strip(),16)
            if self.bbs.get(mod_id) == None:
                self.bbs[mod_id] = []
            self.bbs[mod_id].append(bb_start)
            tmp_line = f.readline().decode('utf-8').strip()
            
            

            
