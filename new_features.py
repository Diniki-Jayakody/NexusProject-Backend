import re

# BASIC LEVEL FEATURES

# B_feature1: Syntax Fundamentals
def mentions_syntax_basics(text):
    patterns = [
        r'\bint\b',r'\bfloat\b', r'\bchar\b', r'\bboolean\b', r'\bif\b', r'\belse\b',
        r'\bwhile\b', r'\bfor\b', r'\bvoid\b', r'\bswitch\b', r'==', r'!=', r'>=', r'<=', r';'
    ]
    return int(any(re.search(p, text) for p in patterns))

# B_feature2: Variables & Types
def mentions_variables_and_types(text):
    patterns = [r'\bvariable\b', r'\bdeclare\b', r'\btype\b', r'\bint\b', r'\bfloat\b', r'\bstring\b',
    r'\bchar\b', r'\boolean\b', r'\bdouble\b'
    ]
    return int(any(re.search(p, text) for p in patterns))

# B_feature3: Control Structures
def mentions_control_structures(text):
    patterns = [r'\bif\b', r'\belse\b', r'\bfor\b', r'\bwhile\b', r'\bswitch\b']
    return int(any(re.search(p, text) for p in patterns))

# B_feature4: Basic Input/Output
def mentions_basic_io(text):
    patterns = [r'\binput\b', r'\boutput\b', r'\bprint\b', r'\bscanner\b', r'\bSystem\.out\.println\b']
    return int(any(re.search(p, text) for p in patterns))

# B_feature5: Functions & Methods
def mentions_functions(text):
    patterns = [r'\bfunction\b', r'\bmethod\b', r'\bvoid\b', r'\breturn\b'
    r'\bparameter\b', r'\bargument\b'
    ]
    return int(any(re.search(p, text) for p in patterns))

# B_feature6: Array/List Handling
def mentions_arrays_or_lists(text):
    patterns = [r'\barray\b', r'\blist\b', r'\bindex\b', r'\biterate\b'
    r'\bindexing\b', r'\bslice\b', r'\bslicing\b', r'\biteration\b'
    ]
    return int(any(re.search(p, text) for p in patterns))

# B_feature7: Simple Algorithms
def mentions_simple_algorithms(text):
    patterns = [r'\bsum\b', r'\bfactorial\b', r'\baverage\b', r'\bcount\b' ,
    r'\bprime (number|check|test)\b', r'\blinear search\b',
    r'\b(sum|add)\b.*\b(numbers|array|list)\b'
    ]
    return int(any(re.search(p, text) for p in patterns))

# B_feature8: Debugging & Syntax Errors
def mentions_debugging_errors(text):
    patterns = [r'\bsyntax error\b', r'\bmissing\b', r'\bdebug\b', r'\bexception\b',
    r'\b(missing semicolon|unbalanced bracket|syntax error|unexpected token)\b',
    r'\b(infinite loop|off-by-one|off by one)\b'
    ]
    return int(any(re.search(p, text) for p in patterns))

# B_feature9: Naming & Style
def mentions_naming_style(text):
    patterns = [r'\bnaming convention\b', r'\bcamel case\b', r'\bsnake case\b',
    r'\bindentation\b', r'\bindent\b'
    ]
    return int(any(re.search(p, text) for p in patterns))

# B_feature10: Pattern-Based Tasks
def mentions_pattern_tasks(text):
    patterns = [r'\bpyramid\b', r'\btriangle\b', r'\bpattern\b', r'\bnumber series\b']
    return int(any(re.search(p, text) for p in patterns))


# ------------------------
# INTERMEDIATE LEVEL FEATURES
# ------------------------

def mentions_data_structures(text):
    patterns = [r'\bstack\b', r'\bqueue\b', r'\bmap\b', r'\bdictionary\b', r'\bset\b',
    r'\btree\b', r'\bgraph\b',r'\bpriority queue\b', r'\bhash table\b',r'\badjacency list\b',
    r'\bDFS\b', r'\bBFS\b',r'\bbinary tree\b',r'\bbalanced tree\b'
    ]
    return int(any(re.search(p, text) for p in patterns))

def mentions_common_algorithms(text):
    patterns = [r'\bsorting\b', r'\brecursion\b', r'\bbinary search\b',
    r'\bmerge sort\b', r'\bquick sort\b', r'\bheap sort\b', r'\bdynamic\b'
    ]
    return int(any(re.search(p, text) for p in patterns))

def mentions_oop_concepts(text):
    patterns = [r'\bclass\b', r'\binheritance\b', r'\bobject\b', r'\bpolymorphism\b'
    r'\babstraction\b', r'\bencapsulation\b',  r'\bconstructor\b',r'\bthis\b',r'\boverriding\b',
    r'\boverloading\b',r'\binterface\b',r'\baccess modifier\b'
    ]
    return int(any(re.search(p, text) for p in patterns))

def mentions_code_design(text):
    patterns = [r'\bmodular\b', r'\bnamespace\b', r'\bpackage\b']
    return int(any(re.search(p, text) for p in patterns))

def mentions_memory_and_performance_concern(text):
    patterns = [r'\bcomplexity\b', r'\bBig[- ]?O\b',r'\bstack\b',r'\bheap\b',r'\bmemory\b']
    return int(any(re.search(p, text) for p in patterns))

def mentions_file_handling(text):
    patterns = [r'\bread\b', r'\bwrite\b', r'\bfile\b', r'\bJSON\b', r'\bCSV\b', r'\bfile handling\b',
    r'\bopen\(.+\)',r'\bwith open\b', r'\breadlines\b', r'\bcontext manager\b',r'\bfile path\b',
    r'\bparsing\b',r'\bJSON parsing\b',r'\bXML\b'
    ]
    return int(any(re.search(p, text) for p in patterns))

def mentions_concurrency_basics(text):
    patterns = [r'\bthread\b', r'\bconcurrent\b', r'\basync\b']
    return int(any(re.search(p, text) for p in patterns))

def mentions_testing_tools(text):
    patterns = [r'\bunit test\b', r'\bpytest\b', r'\bjunit\b',
    r'\bassert\b', r'\btest case\b', r'\btest coverage\b' , r'\bmock\b', r'\bintegration testing\b'
    ]
    return int(any(re.search(p, text) for p in patterns))

def mentions_api_usage(text):
    patterns = [r'\bREST\b', r'\bAPI\b', r'\bGET\b', r'\bPOST\b', r'\bPUT\b', r'\bDELETE\b',
    r'\bendpoint\b', r'\bAPI call\b'r'\bAPI authentication\b', r'\bAPI key\b', r'\bfetch\b', r'\bREST endpoint\b',
    r'\bconsume API\b', r'\bJSON response\b'
    ]
    return int(any(re.search(p, text) for p in patterns))

def mentions_version_control(text):
    patterns = [r'\bgit\b', r'\bcommit\b', r'\bbranch\b']
    return int(any(re.search(p, text) for p in patterns))

def mentions_standard_libraries(text):
    patterns = [r'\bstdlib\b', r'\bsys.argv\b', r'\argparse\b']
    return int(any(re.search(p, text) for p in patterns))


# --------------------------
# Advanced Feature Functions
# --------------------------

def mentions_advanced_algorithms(text):
    patterns = [
        r'\bA\*\b', r'\bFloyd[\s-]?Warshall\b', r'\btopological sort\b', r'\bmax flow\b',
        r'\bmin cut\b', r'\bmatrix chain\b', r'\btraveling salesman\b', r'\bTSP\b',
        r'\bparallel algorithm\b', r'\bDP optimization\b'
    ]
    return int(any(re.search(p, text, re.IGNORECASE) for p in patterns))

def mentions_system_design(text):
    patterns = [
        r'\bmicroservices\b', r'\bevent[-\s]?driven\b', r'\bCQRS\b', r'\bSOA\b',
        r'\bscalability\b', r'\bload balancing\b', r'\bsharding\b', r'\bcaching\b',
        r'\breplication\b', r'\bCDN\b'
    ]
    return int(any(re.search(p, text, re.IGNORECASE) for p in patterns))

def mentions_distributed_systems(text):
    patterns = [
        r'\bKafka\b', r'\bZookeeper\b', r'\bconsensus\b', r'\bPaxos\b', r'\bRaft\b',
        r'\bCAP theorem\b', r'\beventual consistency\b', r'\bvector clock\b',
        r'\bdistributed system\b'
    ]
    return int(any(re.search(p, text, re.IGNORECASE) for p in patterns))

def mentions_manual_memory(text):
    patterns = [
        r'\bmalloc\b', r'\bpointer\b', r'\balloc\b', r'\bfree\b', r'\bmemory model\b',
        r'\block[-\s]?free\b', r'\bCAS\b', r'\bkernel bypass\b', r'\bRDMA\b'
    ]
    return int(any(re.search(p, text, re.IGNORECASE) for p in patterns))

def mentions_metaprogramming(text):
    patterns = [
        r'\breflection\b', r'\bmacro\b', r'\bAST manipulation\b', r'\bcode generation\b',
        r'\bDSL\b', r'\binterpreter\b', r'\bcompiler\b', r'\bparsing\b',
        r'\blexing\b', r'\bgrammar\b', r'\bLLVM\b'
    ]
    return int(any(re.search(p, text, re.IGNORECASE) for p in patterns))

def mentions_profiling_optimization(text):
    patterns = [
        r'\bflame graph\b', r'\bJIT\b', r'\bGC overhead\b', r'\bperf\b', r'\bbottleneck\b',
        r'\bvalgrind\b', r'\beBPF\b', r'\bvtune\b', r'\bperformace profiling\b'
    ]
    return int(any(re.search(p, text, re.IGNORECASE) for p in patterns))

def mentions_security_cryptography(text):
    patterns = [
        r'\bXSS\b', r'\bSQL injection\b', r'\bsanitization\b', r'\bAES\b', r'\bRSA\b',
        r'\bhashing\b', r'\bdigital signature\b', r'\bPKI\b', r'\binput validation\b'
    ]
    return int(any(re.search(p, text, re.IGNORECASE) for p in patterns))

def mentions_ci_cd(text):
    patterns = [
        r'\bJenkins\b', r'\bGitHub Actions\b', r'\bCI/CD\b', r'\bGitLab CI\b',
        r'\bcontinuous integration\b', r'\bcontinuous deployment\b'
    ]
    return int(any(re.search(p, text, re.IGNORECASE) for p in patterns))

def mentions_containerization(text):
    patterns = [
        r'\bDocker\b', r'\bKubernetes\b', r'\bcontainer\b', r'\bpod\b', r'\bservice mesh\b',
        r'\bTerraform\b', r'\bAnsible\b', r'\bPulumi\b', r'\bCloudFormation\b', r'\bIaC\b'
    ]
    return int(any(re.search(p, text, re.IGNORECASE) for p in patterns))

def mentions_static_analysis(text):
    patterns = [
        r'\bstatic analysis\b', r'\bSonarQube\b', r'\bCoverity\b', r'\blinter\b',
        r'\bSAST\b', r'\bDAST\b', r'\bmemory profiler\b'
    ]
    return int(any(re.search(p, text, re.IGNORECASE) for p in patterns))

def mentions_scalable_databases(text):
    patterns = [
        r'\bsharding\b', r'\breplication\b', r'\bconsistency model\b', r'\bACID\b', r'\bNoSQL\b'
    ]
    return int(any(re.search(p, text, re.IGNORECASE) for p in patterns))

def mentions_advanced_concurrency(text):
    patterns = [
        r'\bactor model\b', r'\bgoroutine\b', r'\bchannel\b', r'\bCSP\b', r'\breactive streams\b'
    ]
    return int(any(re.search(p, text, re.IGNORECASE) for p in patterns))

def mentions_advanced_networking(text):
    patterns = [
        r'\bQUIC\b', r'\bHTTP/3\b', r'\bgRPC\b', r'\bprotobuf\b', r'\bTCP tuning\b'
    ]
    return int(any(re.search(p, text, re.IGNORECASE) for p in patterns))

def mentions_language_internals(text):
    patterns = [
        r'\bvirtual machine\b', r'\bbytecode\b', r'\bgarbage collector\b',
        r'\bruntime\b', r'\bJIT compilation\b'
    ]
    return int(any(re.search(p, text, re.IGNORECASE) for p in patterns))

def mentions_reliability_engineering(text):
    patterns = [
        r'\bcircuit breaker\b', r'\bchaos engineering\b', r'\bretry pattern\b', r'\bfault tolerance\b'
    ]
    return int(any(re.search(p, text, re.IGNORECASE) for p in patterns))



